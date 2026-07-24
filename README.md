# QGIS Web Map Exporter

_(Note: please come back later - still at early stages of development!)_

A QGIS 4.x Plugin to export data (in cloud-native formats) and QGIS styling to build a standalone web map. Design aims:

- Convert a QGIS Project to the key components to build a standalone web map with optimized data loading and layer styling as close to QGIS as possible.
- Data can be exported in selected cloud-native data formats. Styles are exported as SLD to enable use of SLDReader for accurate rendering of many different types of QGIS styles in OpenLayers.
- Directly generate a pre-configured HTML/JS template for rendering the map using just a standard web server, whilst allowing selective data/styling updates to be exported from QGIS.
