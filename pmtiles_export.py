# -*- coding: utf-8 -*-
"""
***************************************************************************
WebMapExporter - A QGIS plugin
Export data (in cloud-native formats) and QGIS styling to build a standalone web map

This file is largely copied/adapted from sections of exporter.py in
John Zastrow's MapSplat plugin:
https://github.com/johnzastrow/mapsplat4/blob/main/exporter.py

    copyright            : (C) 2026 by Richard Thomas
    git sha              : $Format:%H$

 ***************************************************************************
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 ***************************************************************************
Export QGIS layers to PMTiles format (copied/adapted from MapSplat plugin).
 """

import os
import sys
import subprocess

# Windows: hide console window when spawning subprocesses
if sys.platform == "win32":
    # Use numeric values to ensure compatibility
    STARTUPINFO = subprocess.STARTUPINFO()
    STARTUPINFO.dwFlags |= 0x00000001  # STARTF_USESHOWWINDOW
    STARTUPINFO.wShowWindow = 0  # SW_HIDE
    CREATIONFLAGS = 0x08000000  # CREATE_NO_WINDOW
else:
    STARTUPINFO = None
    CREATIONFLAGS = 0

from qgis.core import (
    QgsProject,
    QgsVectorFileWriter,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsCoordinateTransformContext,
)

class PMTilesExport:
    """Export QGIS layers to PMTiles files via OGC GeoPackage."""

    def __init__(self, plugin):
        """Initialize PMTiles file exporter.

        :param plugin: QGIS plugin instance
        """
        self.dlg = plugin.dlg
        self.iface = plugin.iface
        self.tr = plugin.tr
        self.project = QgsProject.instance()

        # Target CRS (Web Mercator)
        # TBD: make configurable as using OpenLayers
        self.target_crs = QgsCoordinateReferenceSystem("EPSG:3857")

    def export_single_pmtiles(self, layer, output_dir):
        """Export single vector layer to a PMTiles file."""
        sanitized_layer_name = self._sanitize_layer_name(layer.name())
        self.dlg.log_message(f"Processing PMTiles layer: {layer.name()}...")

        # Export single layer to GeoPackage (clipped to export extent)
        gpkg_path = os.path.join(output_dir, f"{sanitized_layer_name}.gpkg")
        self._export_to_geopackage([layer], gpkg_path)

        # Convert to PMTiles
        pmtiles_path = os.path.join(output_dir, f"{sanitized_layer_name}.pmtiles")
        success = self._convert_to_pmtiles(gpkg_path, pmtiles_path)

        if not success:
            self.dlg.log_message(f"Failed to convert {sanitized_layer_name}")
            return None

        # Clean up intermediate GeoPackage
        if os.path.exists(gpkg_path):
            os.remove(gpkg_path)

        return f"{sanitized_layer_name}.pmtiles"

    def _export_to_geopackage(self, layers, gpkg_path, clip_rect=None):
        """Export vector layers to a GeoPackage.

        :param layers: List of QgsVectorLayer
        :param gpkg_path: Output GeoPackage path
        :param clip_rect: Optional QgsRectangle in EPSG:3857 to spatially clip features
        """
        transform_context = QgsCoordinateTransformContext()

        for i, layer in enumerate(layers):
            layer_name = self._sanitize_layer_name(layer.name())
            self.dlg.log_message(f"  Exporting: {layer.name()} -> {layer_name}")

            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = "GPKG"
            options.layerName = layer_name
            options.fileEncoding = "UTF-8"

            # Set action mode (create or append)
            if i == 0:
                options.actionOnExistingFile = QgsVectorFileWriter.ActionOnExistingFile.CreateOrOverwriteFile
            else:
                options.actionOnExistingFile = QgsVectorFileWriter.ActionOnExistingFile.CreateOrOverwriteLayer

            # Transform to Web Mercator. Reproject from ANY valid source CRS; a layer
            # with an invalid/unset CRS can't be placed on a web map, so warn and skip
            # it (rather than emit points at null island or a dangling source).
            src_crs = layer.crs()
            if not src_crs.isValid():
                self.dlg.log_message(
                    f"  Skipping '{layer_name}': layer has no valid CRS — set one in QGIS "
                    f"(Layer Properties ▸ Source) and re-export."
                )
                continue
            if src_crs != self.target_crs:
                options.ct = QgsCoordinateTransform(
                    src_crs,
                    self.target_crs,
                    self.project
                )

            # Clip to export extent (filterExtent is in destination CRS = EPSG:3857)
            if clip_rect is not None:
                options.filterExtent = clip_rect

            error, error_message, *_ = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer,
                gpkg_path,
                transform_context,
                options
            )
            if error != QgsVectorFileWriter.WriterError.NoError:
                self.dlg.log_message(f"  Warning: {error_message}")

    def _convert_to_pmtiles(self, gpkg_path, pmtiles_path):
        """Convert GeoPackage to PMTiles using ogr2ogr (blocking version for thread).

        :param gpkg_path: Input GeoPackage path
        :param pmtiles_path: Output PMTiles path
        :returns: True if successful
        """
        from qgis.PyQt.QtCore import QCoreApplication

        # Check GDAL version first
        gdal_version = self._check_gdal_version()
        if gdal_version:
            self.dlg.log_message(f"  GDAL version: {gdal_version}")

        # Check if PMTiles driver is available
        if not self._check_pmtiles_driver():
            self.dlg.log_message(
                "PMTiles driver not available. GDAL 3.8+ required."
            )
            return False

        # Show input file size
        gpkg_size_mb = os.path.getsize(gpkg_path) / (1024 * 1024)
        self.dlg.log_message(f"  GeoPackage size: {gpkg_size_mb:.1f} MB",)

       # List layers in GeoPackage
        layers_in_gpkg = self._list_gpkg_layers(gpkg_path)
        if layers_in_gpkg:
            self.dlg.log_message(f"  Layers to convert: {', '.join(layers_in_gpkg)}",)
        else:
            self.dlg.log_message("  Warning: Could not list layers in GeoPackage",)

        # Normalize paths for Windows
        gpkg_path = os.path.normpath(gpkg_path)
        pmtiles_path = os.path.normpath(pmtiles_path)
        output_dir = os.path.dirname(pmtiles_path)

        # Build ogr2ogr command
        #max_zoom = self.settings.get("max_zoom", 6)
        max_zoom = 17 # TBD: make this configurable in the UI

        self.dlg.log_message(f"  Max zoom: {max_zoom}",)
        self.dlg.log_message(f"  Output: {pmtiles_path}",)
        self.dlg.log_message("  Starting ogr2ogr to convert GPKG to PMTile...",)

        # The GeoPackage is always written in EPSG:3857 by _export_to_geopackage
        # (QgsVectorFileWriter applies options.ct to reproject every layer).
        # Specifying -s_srs EPSG:3857 prevents ogr2ogr from attempting a second
        # reprojection when the CRS WKT stored by QGIS is not recognised by GDAL
        # as exactly EPSG:3857 — which would cause visible geometry distortion.
        pmtile_convert_args = [
            "ogr2ogr",
            "-f", "PMTiles",
            "-dsco", "MINZOOM=0",
            "-dsco", f"MAXZOOM={max_zoom}",
            "-s_srs", "EPSG:3857",
            "-t_srs", "EPSG:3857",
            pmtiles_path,
            gpkg_path
        ]

        self.dlg.log_message(f"  Command: {' '.join(pmtile_convert_args)}",)

        try:
            result = subprocess.run(  # nosec B603 B607
                pmtile_convert_args,
                capture_output=True,
                text=True,
                startupinfo=STARTUPINFO,
                creationflags=CREATIONFLAGS
            )
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr.strip() else result.stdout.strip()
                if not error_msg:
                    error_msg = f"ogr2ogr exited with code {result.returncode}"
                self.dlg.log_message(f"  ogr2ogr error: {error_msg}",)
                return False
        except Exception as e:  # nosec B110
            self.dlg.log_message(f"  Exception while running ogr2ogr: {str(e)}",)
            return False

        # Show output file size
        if os.path.exists(pmtiles_path):
            pmtiles_size_mb = os.path.getsize(pmtiles_path) / (1024 * 1024)
            self.dlg.log_message(f"  PMTiles size: {pmtiles_size_mb:.1f} MB",)

        return True

    def _check_gdal_version(self):
        """Check GDAL version.

        :returns: Version string or None
        """
        try:
            result = subprocess.run(  # nosec B603 B607
                ["ogr2ogr", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
                startupinfo=STARTUPINFO,
                creationflags=CREATIONFLAGS
            )
            if result.returncode == 0:
                # Parse "GDAL 3.8.0, released 2023/..."
                return result.stdout.split(",")[0].strip()
        except Exception:  # nosec B110
            pass
        return None

    def _check_pmtiles_driver(self):
        """Check if PMTiles driver is available.

        :returns: True if available
        """
        try:
            result = subprocess.run(  # nosec B603 B607
                ["ogr2ogr", "--formats"],
                capture_output=True,
                text=True,
                timeout=10,
                startupinfo=STARTUPINFO,
                creationflags=CREATIONFLAGS
            )
            return "PMTiles" in result.stdout
        except Exception:
            return False

    def _list_gpkg_layers(self, gpkg_path):
        """List layers in a GeoPackage.

        :param gpkg_path: Path to GeoPackage
        :returns: List of layer names or empty list
        """
        try:
            result = subprocess.run(  # nosec B603 B607
                ["ogrinfo", "-so", "-q", gpkg_path],
                capture_output=True,
                text=True,
                timeout=30,
                startupinfo=STARTUPINFO,
                creationflags=CREATIONFLAGS
            )
            if result.returncode == 0:
                # Parse output like "1: layer_name (Multi Polygon)"
                layers = []
                for line in result.stdout.strip().split("\n"):
                    if line.strip():
                        # Extract layer name between ": " and " ("
                        parts = line.split(": ", 1)
                        if len(parts) > 1:
                            layer_name = parts[1].split(" (")[0]
                            layers.append(layer_name)
                return layers
        except Exception:  # nosec B110
            pass
        return []

    def _sanitize_layer_name(self, name):
        """Sanitize layer name for use in files/PMTiles.

        :param name: Original layer name
        :returns: Sanitized name
        """
        # Replace spaces and special chars with underscores
        sanitized = "".join(c if c.isalnum() or c == "_" else "_" for c in name)

        # Remove consecutive underscores
        while "__" in sanitized:
            sanitized = sanitized.replace("__", "_")

        # Remove leading/trailing underscores
        sanitized = sanitized.strip("_")
        return sanitized
