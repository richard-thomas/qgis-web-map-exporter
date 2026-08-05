# -*- coding: utf-8 -*-
"""Export QGIS layers and styling to files in a selected folder."""

import json
import os
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

class FileExport:
    """Perform data and styling extraction from QGIS into files."""

    def __init__(self, plugin=None):
        self.plugin = plugin
        self.last_output_dir = None

    def export_layers(self, dialog, iface, tr):
        """Prompt for an output folder and write requested export files."""

        # Get selected layers and their requested export formats from UI
        root = dialog.layers_tree_qt.invisibleRootItem()
        selected_layers = []
        for index in range(root.childCount()):
            item = root.child(index)
            self._collect_selected_layers(dialog, item, selected_layers)

        # If GeoParquet export is requested, stop export if not supported
        if (not self.is_geoparquet_wr_supported() and #not self.is_geoparquet_io_supported() and
                any(layer_format == "GeoParquet" for _, _, layer_format in selected_layers)):
            dialog.log_text_browser_qt.append(
                "GeoParquet export is not supported by the current QGIS installation.\n"
                "Please install the 'Parquet' GDAL driver to enable GeoParquet export."
            )
            iface.messageBar().pushMessage(
                "Error",
                "Export aborted: GeoParquet export is not supported by the current QGIS installation.",
                level=Qgis.Critical)
            return

        # Get Output folder to write files from user
        if self.last_output_dir is None:
            self.last_output_dir = QgsProject.instance().absolutePath() or os.path.expanduser("~")

        output_dir = QFileDialog.getExistingDirectory(
            dialog,
            tr("Select export folder"),
            self.last_output_dir,
        )
        if not output_dir:
            return
        self.last_output_dir = output_dir

        # Write SLD files for selected layers if requested
        write_slds = dialog.options_checkbox_slds_qt.isChecked()
        if write_slds:
            dialog.log_text_browser_qt.append(
                f"Exporting SLD files for selected layers to: {output_dir}"
            )
            for layer_name, layer, _ in selected_layers:
                if layer is None:
                    continue
                sld_text = self.get_layer_sld(layer)
                if sld_text is None:
                    continue
                sld_output_path = os.path.join(output_dir, f"{layer_name}.sld")
                with open(sld_output_path, "w", encoding="utf-8") as handle:
                    handle.write(sld_text)

        # Set up data formats options
        transform_context = QgsCoordinateTransformContext()
        fgb_options = QgsVectorFileWriter.SaveVectorOptions()
        fgb_options.driverName = "FlatGeobuf"
        fgb_options.fileEncoding = "UTF-8"
        gpq_options = QgsVectorFileWriter.SaveVectorOptions()
        gpq_options.driverName = "GeoParquet"
        gpq_options.fileEncoding = "UTF-8"
        gj_options = QgsVectorFileWriter.SaveVectorOptions()
        gj_options.driverName = "GeoJSON"
        gj_options.fileEncoding = "UTF-8"

        # Write out data in requested formats
        for layer_name, layer, layer_format in selected_layers:
            if layer is None:
                continue

            if layer_format == "FlatGeoBuf":
                output_path = os.path.join(output_dir, f"{layer_name}.fgb")
                dialog.log_text_browser_qt.append(
                    f"Exporting FlatGeobuf layer: {layer_name}.fgb"
                )
                dialog.log_text_browser_qt.append(f"- Layer source: {layer.source()}")
                QgsVectorFileWriter.writeAsVectorFormatV3(
                    layer, output_path, transform_context, fgb_options
                )
            elif layer_format == "GeoJSON":
                output_path = os.path.join(output_dir, f"{layer_name}.geojson")
                dialog.log_text_browser_qt.append(
                    f"Exporting GeoJSON layer: {layer_name}.geojson"
                )
                QgsVectorFileWriter.writeAsVectorFormatV3(
                    layer, output_path, transform_context, gj_options
                )
            elif layer_format == "PMTile":
                # TBD: Implement PMTile export
                dialog.log_text_browser_qt.append(
                    f'Skipping layer "{layer_name}" - PMTile export not yet implemented'
                )
            elif layer_format == "GeoParquet":
                if self.is_geoparquet_wr_supported():
                    output_path = os.path.join(output_dir, f"{layer_name}.parquet")
                    dialog.log_text_browser_qt.append(
                        f"Exporting GeoParquet layer: {layer_name}.parquet"
                    )
                    QgsVectorFileWriter.writeAsVectorFormatV3(
                        layer, output_path, transform_context, gpq_options
                    )
                elif self.is_geoparquet_io_supported():
                    # TBD: Implement geoparquet-io export
                    dialog.log_text_browser_qt.append(
                        f'Skipping layer "{layer_name}" - geoparquet-io export not yet implemented'
                    )

        # Write map config file
        write_map = dialog.options_checkbox_map_qt.isChecked()
        if write_map:
            dialog.log_text_browser_qt.append(f"Exporting map config file to: {output_dir}")

            # Write a web map configuration JSONP file for the selected layers
            map_config_txt = "var mapConfig = "
            map_config = {}

            # Hardwire projection for now
            map_config["displayProjection"] = "EPSG:3857"

            # Add details of selected layers and compute their maximum extent
            data_layers_config = []
            max_extent = QgsRectangle()
            for layer_name, layer, layer_format in selected_layers:
                data_layers_config.append(
                    {
                        "name": layer_name,
                        "format": layer_format,
                        "sld": f"{layer_name}.sld" if write_slds else None,
                    }
                )
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

        iface.messageBar().pushMessage(
            "Success",
            f"Web Map Export completed to folder: {output_dir}.",
            level=Qgis.Success)
        dialog.log_text_browser_qt.append("Export complete!\n")

    def _collect_selected_layers(self, dialog, item, selected_layers):
        if item.childCount() == 0:
            widget = dialog.layers_tree_qt.itemWidget(item, 0)
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
            selected_layers.append((layer_name, layer_item, layer_format))
            return

        for child_index in range(item.childCount()):
            child_item = item.child(child_index)
            self._collect_selected_layers(dialog, child_item, selected_layers)

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
            return None

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
