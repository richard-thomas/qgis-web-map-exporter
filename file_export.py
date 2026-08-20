# -*- coding: utf-8 -*-
"""
***************************************************************************
WebMapExporter - A QGIS plugin
Export data (in cloud-native formats) and QGIS styling to build a standalone web map

    copyright            : (C) 2026 by Richard Thomas
    git sha              : $Format:%H$

 ***************************************************************************
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 ***************************************************************************
Export QGIS layer data, styling and web map configuration to files in a selected folder.
"""

import json
import os
import re
from pathlib import Path
from osgeo import ogr

from qgis.PyQt.QtWidgets import QCheckBox, QLabel, QComboBox, QFileDialog
from qgis.core import (
    QgsCoordinateTransform,
    QgsCoordinateTransformContext,
    QgsProject,
    QgsRectangle,
    QgsSldExportContext,
    QgsVectorFileWriter,
    Qgis,
)

from .pmtiles_export import PMTilesExport

# Name of subdirectories to hold exported data and styles files
DATA_DIR_NAME = "data"
STYLES_DIR_NAME = "styles"


class FileExport:
    """Export QGIS layer data, styling and web map configuration to files."""

    def __init__(self, dialog, plugin):
        """Initialize general file exporter and PMTiles exporter class.

        :param dialog: QGIS plugin Qt dialog instance
        :param plugin: QGIS plugin instance
        """
        self.dlg = dialog
        self.iface = plugin.iface
        self.tr = plugin.tr
        self.last_output_dir = None
        self.pmtiles_exporter = PMTilesExport(dialog, plugin)

        # Warn if GeoParquet is not supported by the GDAL/OGR installation
        if not self.is_geoparquet_wr_supported():
            self.dlg.log_message(
                "Warning: GeoParquet format is not supported by this GDAL/OGR installation.")
            if not self.is_geoparquet_io_supported():
                self.dlg.log_message(
                    "Warning: geoparquet-io library is not available either.\n"
                    "Exporting to GeoParquet will not be possible.\n")
            else:
                self.dlg.log_message(
                    "However, geoparquet-io library is available, so exporting to GeoParquet will be possible.\n")

    def export_selected_layers(self, ui_options):
        """Prompt for an output folder and write requested export files.

        :param ui_options: settings from plugin options tab
        """
        # Switch tab to log tab so user can see progress messages
        self.dlg.tab_widget_qt.setCurrentWidget(self.dlg.tab_output_qt)
        self.dlg.log_message(
            "\nStarting Web Map Export...")

        # Get selected layers and their requested export formats from UI
        root = self.dlg.layers_tree_qt.invisibleRootItem()
        selected_layers = []
        for index in range(root.childCount()):
            item = root.child(index)
            self._collect_selected_layers(item, selected_layers)

        # Get list of layers in order of rendering (bottom layer first)
        # Define z_index (which gets passed on to web map config) such
        # that by default rendering order is reversed, but user can
        # tweak this manually in map config JSON if desired.
        layers_in_order = QgsProject.instance().layerTreeRoot().layerOrder()
        for layer_info in selected_layers:
            layer = layer_info["item"]
            if layer in layers_in_order:
                layer_info["z_index"] = -layers_in_order.index(layer) - 1
            else:
                layer_info["z_index"] = 0  # Layer not found in rendering order!

        # If GeoParquet export is requested, stop export if not supported
        if (not self.is_geoparquet_wr_supported() and #not self.is_geoparquet_io_supported() and
                any(layer_info["out_format"] == "GeoParquet" for layer_info in selected_layers)):
            self.dlg.log_message(
                "GeoParquet export is not supported by the current QGIS installation.\n"
                "Please install the 'Parquet' GDAL driver to enable GeoParquet export."
            )

            # Put red message in main QGIS window message bar
            self.iface.messageBar().pushMessage(
                "Error",
                "Export aborted: GeoParquet export is not supported by the current QGIS installation.",
                level=Qgis.Critical)
            return

        # Get Output folder to write files from user
        if self.last_output_dir is None:
            self.last_output_dir = QgsProject.instance().absolutePath() or os.path.expanduser("~")
        output_dir = QFileDialog.getExistingDirectory(
            self.dlg,
            self.tr("Select export folder"),
            self.last_output_dir,
        )
        if not output_dir:
            # User has pressed Cancel or hit escape
            return
        self.last_output_dir = output_dir

        # Create output directories for data and SLD styles
        output_data_dir = os.path.join(output_dir, DATA_DIR_NAME)
        try:
            Path(output_data_dir).mkdir(exist_ok=True)
        except Exception as e:
            self.dlg.log_message(f'Export aborted: Error creating "{DATA_DIR_NAME}" directory: {e}')
            return
        output_styles_dir = os.path.join(output_dir, STYLES_DIR_NAME)
        try:
            Path(output_styles_dir).mkdir(exist_ok=True)
        except Exception as e:
            self.dlg.log_message(f'Export aborted: Error creating "{STYLES_DIR_NAME}" directory: {e}')
            return

        # Export SLD files for selected layers if requested
        export_slds = ui_options["export_slds"]
        if export_slds:
            self.dlg.log_message(
                f"Exporting SLD files for selected layers to: {output_styles_dir}"
            )
            for layer_info in selected_layers:
                if layer_info["item"] is None:
                    continue
                sld_text = self.get_layer_sld(layer_info["item"])
                if sld_text is None:
                    continue
                sld_filename = f"{layer_info["name"]}.sld"
                modified_sld_text = self._sld_qgis_tweak(sld_text, layer_info)
                layer_info["style"] = f"{STYLES_DIR_NAME}/{sld_filename}"
                sld_output_path = os.path.join(output_styles_dir, sld_filename)
                with open(sld_output_path, "w", encoding="utf-8") as handle:
                    handle.write(modified_sld_text)

        # Set up data formats options
        transform_context = QgsCoordinateTransformContext()
        fgb_options = QgsVectorFileWriter.SaveVectorOptions()
        fgb_options.driverName = "FlatGeobuf"
        fgb_options.fileEncoding = "UTF-8"
        gpq_options = QgsVectorFileWriter.SaveVectorOptions()
        gpq_options.driverName = "Parquet"
        gpq_options.fileEncoding = "UTF-8"
        gj_options = QgsVectorFileWriter.SaveVectorOptions()
        gj_options.driverName = "GeoJSON"
        gj_options.fileEncoding = "UTF-8"

        # Write out data in requested formats
        for layer_info in selected_layers:
            layer = layer_info["item"]
            layer_name = layer_info["name"]
            layer_format = layer_info["out_format"]

            if layer is None:
                continue

            # Actual filename written to disk (may differ from layer name if sanitized)
            written_filename = None

            if layer_format == "FlatGeoBuf":
                output_path = os.path.join(output_data_dir, f"{layer_name}.fgb")
                self.dlg.log_message(
                    f"Exporting FlatGeobuf layer: {layer_name}"
                )
                self.dlg.log_message(f"- Layer source: {layer.source()}")
                return_code, error_message, written_filename, _ = QgsVectorFileWriter.writeAsVectorFormatV3(
                    layer, output_path, transform_context, fgb_options
                )
                if return_code != QgsVectorFileWriter.NoError:
                    self.dlg.log_message(
                        f"Error exporting FlatGeobuf layer '{layer_name}': {error_message}"
                    )
            elif layer_format == "GeoJSON":
                output_path = os.path.join(output_data_dir, f"{layer_name}.geojson")
                self.dlg.log_message(
                    f"Exporting GeoJSON layer: {layer_name}"
                )
                return_code, error_message, written_filename, _ = QgsVectorFileWriter.writeAsVectorFormatV3(
                    layer, output_path, transform_context, gj_options
                )
                if return_code != QgsVectorFileWriter.NoError:
                    self.dlg.log_message(
                        f"Error exporting GeoJSON layer '{layer_name}': {error_message}"
                    )
            elif layer_format == "PMTile":
                # Any error reporting within export_single_pmtiles()
                written_filename = self.pmtiles_exporter.export_single_pmtiles(
                    layer, output_data_dir, ui_options)
            elif layer_format == "GeoParquet":
                if self.is_geoparquet_wr_supported():
                    output_path = os.path.join(output_data_dir, f"{layer_name}.parquet")
                    self.dlg.log_message(
                        f"Exporting GeoParquet layer: {layer_name}.parquet"
                    )
                    return_code, error_message, written_filename, _ = QgsVectorFileWriter.writeAsVectorFormatV3(
                        layer, output_path, transform_context, gpq_options
                    )
                    if return_code != QgsVectorFileWriter.NoError:
                        self.dlg.log_message(
                            f"Error exporting GeoParquet layer '{layer_name}': {error_message}"
                        )
                elif self.is_geoparquet_io_supported():
                    # TBD: Implement geoparquet-io export
                    self.dlg.log_message(
                        f'Skipping layer "{layer_name}" - geoparquet-io export not yet implemented'
                    )

            if not written_filename:
                self.dlg.log_message(
                    f"- Skipping layer '{layer_name}' - (failed to write file or unsupported format: {layer_format})"
                )
                layer_info["data_url"] = ""
                continue
            data_url = f"{DATA_DIR_NAME}/{Path(written_filename).name}"
            layer_info["data_url"] = data_url
            self.dlg.log_message(f"- Layer source URL: {data_url}")

        # Write map config file
        if ui_options["export_map_config"]:
            self.dlg.log_message(f"Exporting map config file to: {output_dir}")

            # Write a web map configuration JSONP file for the selected layers
            map_config_txt = "var mapConfig = "
            map_config = {}
            map_config["pageTitle"] = ui_options["web_map_title"]

            # Hardwire projection for now
            map_config["displayProjection"] = "EPSG:3857"

            # Add details of selected layers and compute their maximum extent
            data_layers_config = []
            max_extent = QgsRectangle()
            for layer_info in selected_layers:
                layer_name = layer_info["name"]
                data_layers_config.append({
                    "data_url": layer_info["data_url"],
                    "label": layer_info["name"],
                    "style": layer_info["style"] if export_slds else "",
                    "z_index": layer_info["z_index"]
                })
                layer = layer_info["item"]
                if layer.extent():
                    # Convert extent to EPSG:3857 if needed (hardwired for now)
                    if layer.crs().authid() != "EPSG:3857":
                        transform = QgsCoordinateTransform(
                            layer.crs(),
                            QgsProject.instance().crs(),
                            transform_context,
                        )
                        layer_extent_3857 = transform.transform(layer.extent())
                        max_extent.combineExtentWith(layer_extent_3857)
                    else:
                        max_extent.combineExtentWith(layer.extent())

            map_config["initialMapExtent"] = [
                max_extent.xMinimum(),
                max_extent.yMinimum(),
                max_extent.xMaximum(),
                max_extent.yMaximum(),
            ]
            map_config["dataLayersConfig"] = data_layers_config

            map_config_txt += json.dumps(map_config, indent=4)
            map_config_txt += ";\n"
            map_output_path = os.path.join(output_dir, "map_config.js")
            with open(map_output_path, "w", encoding="utf-8") as handle:
                handle.write(map_config_txt)

        # Put green message in main QGIS window message bar
        self.iface.messageBar().pushMessage(
            "Success",
            f"Web Map Export completed to folder: {output_dir}.",
            level=Qgis.Success)
        self.dlg.log_message("Export complete!\n")

    def _collect_selected_layers(self, item, selected_layers):
        """Get information from selected layers (only) of UI dialog."""
        if item.childCount() == 0:
            widget = self.dlg.layers_tree_qt.itemWidget(item, 0)
            if widget is None:
                return

            checkbox = widget.findChild(QCheckBox)
            if checkbox is None or not checkbox.isChecked():
                return

            label_widget = widget.findChild(QLabel)
            layer_name = label_widget.text()
            format_combobox = widget.findChild(QComboBox)
            layer_format = format_combobox.currentText()

            layer_item = self.find_layer_by_name(layer_name)
            selected_layers.append({
                "name": layer_name,
                "item": layer_item,
                "out_format": layer_format
            })
            return

        for child_index in range(item.childCount()):
            child_item = item.child(child_index)
            self._collect_selected_layers(child_item, selected_layers)

    def find_layer_by_name(self, layer_name):
        """Find a layer in the current project by its tree name."""
        for layer in QgsProject.instance().mapLayers().values():
            if layer.name() == layer_name:
                return layer
        return None

    def get_layer_sld(self, layer):
        """Return SLD content for a layer if it is available."""
        if layer is None:
            return None

        try:
            context = QgsSldExportContext()
            sld_text = layer.exportSldStyleV3(context)
            return sld_text.toString()
        except Exception:
            self.dlg.log_message("WARNING: Unable to extract SLD for layer '"
                + layer.name() + "' - layer will not be styled in web map.")
            return None

    def _sld_qgis_tweak(self, sld_text, layer_info):
        """Modify QGIS-exported SLD content to work better with SLDReader JavaScript module."""

        #
        # FIX Raster Image Marker (aka "graphic fill" in SLD):
        # QGIS-exported SLD does not include size & displacement parameters
        #
        # TBD: Handle Categorized or Graduated Renderers, or multiple stacked sub-layers

        # If we find an <ExternalGraphic> element, add size and displacement attributes to the <Graphic> element
        ext_graphic_pattern = re.compile(r'(<se:Graphic>\s+<se:ExternalGraphic>.*?</se:ExternalGraphic>)(\s+</se:Graphic>)', re.DOTALL)
        while ext_graphic_pattern.search(sld_text):
            self.dlg.log_message(
                f"INFO: inserting missing size/displacement for SLD <Graphic> element in '{layer_info['name']}'"
            )

            # Get the overall marker size and displacement (return floats)
            renderer = layer_info['item'].renderer()
            symbol = renderer.symbol()
            marker_size = symbol.size()
            symbol_layer = symbol.symbolLayer(0)
            displacement = symbol_layer.offset()
            x_offset = displacement.x()
            y_offset = displacement.y()

            # Insert size and displacement attributes immediately before end of <Graphic> element
            replacement = (r"\1\n" +
                f"""<!-- Auto fix - START -->
                <se:Size>{marker_size}</se:Size>
                <se:Displacement>
                 <se:DisplacementX>{x_offset}</se:DisplacementX>
                 <se:DisplacementY>{y_offset}</se:DisplacementY>
                </se:Displacement>""" +
                r"\n<!-- Auto fix - END -->\2")
            sld_text = re.sub(ext_graphic_pattern, replacement, sld_text)

        #
        #  FIX SVG Marker: QGIS-exported SLD uses a full local disk path
        #
        # TBD: copy the SVG file to local export folder and point to that

        # Regular Expression to search SLD for ONLY QGIS SVG folder '/svg/'
        # as a local path, i.e. starting with '/' (linux) or 'C:/' (Windows)
        qgis_local_svg_pattern = re.compile(r'(OnlineResource .*xlink:href=)[\\]?"[A-Z]?[:]?\/.*\/svg\/')
        while qgis_local_svg_pattern.search(sld_text):
            self.dlg.log_message(
                f"WARNING: replacing QGIS local SVG path with GitHub version in '{layer_info['name']}.sld'"
            )

            # For now just redirect to QGIS source folders on GitHub which should find
            # QGIS system SVGs (not ideal as slow).
            svg_redirect_folder = "https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg"
            replacement = f'\\1"{svg_redirect_folder}/'
            sld_text = re.sub(qgis_local_svg_pattern, replacement, sld_text)

        #
        #  FIX dot/dash length for pre-defined line dash patterns
        #  (QGIS SLD bug just for predefined dash patterns, i.e. not custom)
        #
        # TBD: detect predefined dash patterns, then scale SLD strokeDasharray values by strokeWidth

        return sld_text

    def is_geoparquet_wr_supported(self):
        """Check whether GeoParquet format is directly supported by QgsVectorFileWriter."""
        if hasattr(self, "geoparquet_wr_supported"):
            return self.geoparquet_wr_supported
        driver = ogr.GetDriverByName("Parquet")
        if driver is None:
            self.geoparquet_wr_supported = False
        else:
            self.geoparquet_wr_supported = driver.TestCapability(ogr.ODrCCreateDataSource)
        return self.geoparquet_wr_supported

    def is_geoparquet_io_supported(self):
        """Check whether geoparquet_io library is available for writing GeoParquet files."""
        if hasattr(self, "geoparquet_io_available"):
            return self.geoparquet_io_available
        try:
            import geoparquet_io  # type: ignore # noqa: F401
            self.geoparquet_io_available = True
        except ImportError:
            self.geoparquet_io_available = False
        return self.geoparquet_io_available
