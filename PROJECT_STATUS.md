# Detailed Status and Viability Notes

## Operational limitations

Planned but still to be implemented (in order of priority):
- **SVG Files:** Write SVG files to the output folder. (As a temporary workaround QGIS built-in SVGs are currently automatically redirected in the web map to the original QGIS files on GitHub. A warning of this is given in the 'Output Log' tab).
- Supporting online data sources (remaining online in web map)
- Option: Merge SLDs into a single file (and adapt JS code)
- Option: Merge PMTiles into single layer file
- Layer attribute selection for export (similar to qgis2web approach) for data saving (and later pop-up support)
- Adding clipping extent (defaulting to layer extent)
- Optionally exporting online data (clipped) to files
- Adding "Select All" to Layers tab to select (or unselect) all layers + groups
- Option: Make GeoJSON RFC7946 compliant
- JS support for GeoParquet
- geoparquet_io write support

Under consideration (in order of priority), mainly if plugin taken beyond "proof of concept":
- SLD: consider using [QGIS SLD exportContext](https://qgis.org/pyqgis/master/core/QgsSldExportContext.html#qgis.core.QgsSldExportContext) to set options like exporting complex patterns as PNG/SVG
- Raster support
- Explicit Basemap support from online WMS/XYZ/Vector Tile
- Adding "Force all layer formats" UI with combiBox
- Option: Specify GeoJSON precision (dp) if not RFC7946 compliant
- Web map pop-up support
- Exporting legend symbol items (for web map legend + layer selector)

## Styling limitations

Note: for illustrated examples of some of the (current) styling limitations, see the example web map pages.

For details on the fundamental SLD styling limitations of QGIS and the SLD Reader library, see: [ol-sld-styler Styling Limitations](https://github.com/richard-thomas/ol-sld-styler/blob/main/StylingLimitations.md). Many of the workarounds given in that document are specific to ol-sld-styler, but give an indication of what might be possible to implement in the "Web Exporter" QGIS plugin. In particular, because the plugin has access to the source QGIS layers (unlike ol-sld-styler) it should be able to make up for some of the problems with the raw QGIS SLD export.

Current styling limitations of Web Map Exporter in addition to those listed in [ol-sld-styler Styling Limitations](https://github.com/richard-thomas/ol-sld-styler/blob/main/StylingLimitations.md) (or that are potentially fixable in this plugin) include (in order of priority to address):
- **Dash pattern lines:** [FIXABLE] incorrect dot/dash spacing of predefined (but not custom) dash patterns as these are incorrectly not scaled by stroke width (QGIS bug)
- **SVGs/PNG rendering:** [FIXABLE] on web map loading any symbology using SVGs or PNGs is currently not not rendered but appears when the map is first panned or zoomed (SLDReader requires a callback to be set up to fix this)
- **PNG markers:** [FIXABLE?] PNGs (unless embedded) are not exported by QGIS in SLD
- **Label word wrap:** Word wrap settings on labels not in web map
- **Label overlap:** Labels overlap when zoomed out. Although you could set 'declutter' for layers in OpenLayers this would also hide overlapping features.
- **Line label placement:** labels above line in QGIS are placed on line
- **Label callouts:** not supported

## Viability as a production plugin

If development was continued along the current SLD Reader-based path:
- In the current examples, the QGIS style matching seems to be quite promising, but requires users to use some QGIS styling methods in particular ways (and avoid some styling types altogether).
- Current test examples are very small and localized data sets so do not give any indication of how well the cloud-native data formats will perform.
- For faster loading (particularly with large numbers of small layers), the planned merging of SLD files and merging PMTiles files should help.
- For simplicity of development, the JavaScript libraries are currently loaded in their entirety using the ```<script>``` tag. If they were instead loaded as ES modules and combined with a bumndler like Vite or Webpack then this would result in discarding of unused code, fewer download files and thus faster web map loading. It would also allow OpenLayers 10+ to be used (issues with the PMTiles OpenLayers library restricts it to using OpenLayers 9 with script loading).

However, my biggest question is whether switching the core styling engine from SLD Reader to [GeoStyler](https://geostyler.org/) would improve things (especially in the long term)...

Pros:
- GeoStyler would allow use of MapLibre GL JS which could be more lightweight and faster than OpenLayers
- GeoStyler can read QGIS native QML style format and includes support for potentially more data-defined styling than SLD would provide in its QGIS-exported rules/expressions.
- It will undoubtedly have improved since I last did an in-depth test of it in August 2020, but is it now better at QGIS styling than SLD Reader?

Cons:
- If using GeoStyler, for reduced web map loading time and faster rendering, it would be best for the plugin to write out styles in GeoStyler intermediate style format, so the plugin would need to call on the GeoStyler CLI (which a user would have to manually install).
- The QGIS QML style format has changed significantly in the move from QGIS 3 to 4, so this might have impaired (for now) GeoStyler's ability to import QGIS 4 QML, though could try it with QGIS-exported SLD.