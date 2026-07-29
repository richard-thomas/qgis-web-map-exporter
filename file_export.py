# -*- coding: utf-8 -*-
"""Export QGIS layers and styling to files in a selected folder."""

import json
import os

from qgis.PyQt.QtWidgets import QCheckBox, QLabel, QComboBox, QFileDialog
from qgis.core import (
    QgsCoordinateTransform,
    QgsCoordinateTransformContext,
    QgsProject,
    QgsRectangle,
    QgsSldExportContext,
    QgsVectorFileWriter,
)


class FileExport:
    """Perform data and styling extraction from QGIS into files."""

    def __init__(self, plugin=None):
        self.plugin = plugin
        self.last_output_dir = None

    def export_layers(self, dialog, tr):
        """Prompt for an output folder and write requested export files."""
        if dialog is None:
            return

        dialog.log_text_browser_qt.append("\nGetting output folder from user for exporting...")
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

        selected_layers = self.collect_selected_layers(dialog)

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

        transform_context = QgsCoordinateTransformContext()
        fgb_options = QgsVectorFileWriter.SaveVectorOptions()
        fgb_options.driverName = "FlatGeobuf"
        fgb_options.fileEncoding = "UTF-8"
        gj_options = QgsVectorFileWriter.SaveVectorOptions()
        gj_options.driverName = "GeoJSON"
        gj_options.fileEncoding = "UTF-8"

        for layer_name, layer, layer_format in selected_layers:
            if layer is None:
                continue

            if layer_format == "FlatGeoBuf":
                output_path = os.path.join(output_dir, f"{layer_name}.fgb")
                dialog.log_text_browser_qt.append(
                    f"Exporting FlatGeobuf layer: {layer_name}.fgb"
                )
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
                dialog.log_text_browser_qt.append(
                    f'Skipping layer "{layer_name}" - PMTile export not yet implemented'
                )
            elif layer_format == "GeoParquet":
                dialog.log_text_browser_qt.append(
                    f'Skipping layer "{layer_name}" - GeoParquet export not yet implemented'
                )

        write_map = dialog.options_checkbox_map_qt.isChecked()
        if write_map:
            dialog.log_text_browser_qt.append(f"Exporting map config file to: {output_dir}")

            map_config_txt = "var mapConfig = "
            map_config = {}
            map_config["displayProjection"] = "EPSG:3857"

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

        dialog.log_text_browser_qt.append("Export complete!\n")

    def collect_selected_layers(self, dialog):
        """Collect checked layers from the tree widget rows."""
        root = dialog.layers_tree_qt.invisibleRootItem()
        selected_layers = []
        for index in range(root.childCount()):
            item = root.child(index)
            self._collect_selected_layers(dialog, item, selected_layers)
        return selected_layers

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
