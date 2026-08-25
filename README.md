# QGIS Web Map Exporter

_(Note: please come back in a week or so - initial site is still in development!)_

A "Proof of Concept" QGIS 4.x Python Plugin to export standalone interactive web maps with faithful QGIS styling, exporting data in cloud-native formats

![QGIS vs web browser styling](images/QGIS%20+%20Firefox%20D+S%20Canal%20screengrab.png)
    _Example web map browser rendering (inset) vs original QGIS Project_

 For a wider discussion of existing open source QGIS-styling web map solutions and the motivation for developing this plugin, see my LinkedIn article:
- [Faithfully QGIS-styled Web Maps with Cloud-Native Data](TBD-Add-cross-ref-to-LinkedIn-article).

## Key Design Aims

- **"Instant" web maps:** Convert a QGIS Project to the key components to build a complete standalone interactive web map which can be immediately viewed in a web browser (as with the [qgis2web](https://github.com/qgis2web/qgis2web/blob/master/README.md) and [MapSplat](https://github.com/johnzastrow/mapsplat4/blob/main/README.md) plugins).
- **QGIS Styling:** Accurately style (vector) data layers to match QGIS Desktop as closely as possible (for a wide range of styling types).
- **Cloud-Native Data:** Export data in selectable cloud-native file formats to optimize partial data loading from cheap online storage (e.g. cloud object/blob storage such as AWS S3 buckets or simple web servers).
- **Performance:** Test the viability of such cheap data sourcing for realistic performant web maps: do they make a viable alternative to the dependency on dedicated database and geospatial application servers and their inherent costs, set-up and maintenance requirements?

(Note that this plugin is not currently available in the QGIS Plugin Repository, but you can manually install it yourself - see [Installation](#installation))

## Current Status

The key components of the plugin are now operational, exporting an instantly-viewable web map from a QGIS project. You can now try it out yourself (see [Quick Start Guide](#quick-start-guide) below). See my **Detailed Status and Viability Notes** (Link TBD) for a more in-depth discussion of this proof of concept.

Key features include:
- Qt6 Python Plugin Dialog dynamically populated with QGIS project layers
- Data export in layer-selectable format of: cloud-native FlatGeoBuf/PMTiles/GeoParquet or GeoJSON
- Styling export as SLD files for each layer, with some post-processing to handle QGIS quirks
- Web Map Configuration export as a JSONP file
- Web Map rendering with OpenLayers of all exported data formats (except GeoParquet)
- Web Map styling using the [SLDReader](https://github.com/NieuwlandGeo/SLDReader/blob/master/README.md) library



The status of the **styling** is easiest to get an idea of by looking at examples of 2 QGIS projects I had to hand and their resultant exported web maps:
- (MRCO Site Map - Link TBD): detailed layout of a community orchard including a wide variety of polygon fill styles and zoom-level labelling changes
- (Dorset & Somerset Canal - Link TBD): evidences for a former canal route with lots of overlapping features with complex rule-based styling by feature type and zoom level

To test the handling and performance of the cloud-native data format usage, I now need to try it out with much larger datasets.

## Installation

Being at a "Proof of Concept" stage, this is not available in the QGIS Plugin Repository (so cannot be directly installed from the Plugins menu in QGIS). However, if you want to try it out you can manually install it by downloading this repository and either placing it the QGIS plugins folder or your own development folder. Full platform-specific details are given in Jonah Sullivan's helpful [Plugin Builder (Deploying)](https://jonah-sullivan.github.io/Qgis-Plugin-Builder/#deploying) instructions.

## Quick Start Guide

After installing the plugin, within QGIS 4.x:
- Open the plugin dialog from the plugins toolbar or from menu:
    - Web > Web Map Exporter > Export data and styling

_TBD: insert Plugin screengrab ("Layers" tab)_

- (If you had a project already loaded, your map layers will automatically have been loaded into the plugin 'Layers' panel).
- Otherwise press 'Reload Layers' (or do this if you change project layers later).
- In Layers tab, select (currently just vector) layers you want to export and the desired output data format for each layer:
    - **PMTiles:** Cloud-native vector tile format that creates simplified data for more zoomed out levels to enable fast data loading of just the current view.
    - **FlatGeoBuf:** Cloud-native lossless format that enables partial loading of data for current view. To prevent excessive data loads, any large files should be styled to only display when the view is more zoomed-in.
    - **GeoParquet:** Cloud-native lossless columnar format that enables partial loading of data for current view. Best avoided for now: many installations of QGIS lack the required GDAL driver to export it and not implemented in the web map yet as no direct OpenLayers support.
    - **GeoJSON:** Human readable/editable format suitable for small and simple datasets, but must be loaded completely and can be slow to load and render for larger datasets.
- Select 'Options' tab:

_TBD: insert Plugin screengrab ("Options" tab)_

- Make any required adjustments in the 'Options' tab, including:
    - **PMTiles Max Zoom:** keeping this low reduces file size, but increases geometry simplification errors when zoomed in.
    - **Output Display Projection:** Allows the web map to use local coordinate systems for truer rendering. Note that the PMTiles format is inherently fixed at EPSG:3857 (Web Mercator) so only use that (the default field value) if you want to use any PMTiles layers.
- Press 'Export' button to write out data and/or styling and/or map configuration JSON (as selected in Options)
    - (A "Select Export Folder" file selector dialog will open)
    - Select a (preferably empty) folder that you want to export the files to and click 'Open'
    - (The plugin will switch to the 'Output Log' tab to give details of the progress of the export process).
    - Check the output log for any ERROR or WARNING messages.

On successful completion of the export you should see 3 things in your export folder:
- 'data' sub-folder: contains all the exported data files
- 'styles' sub-folder: contains all the SLD styling files
- 'map_config.js': JSONP web map configuration file

Copy the 2 template files from the plugin "web_map_viewer" folder into your export folder:
- web_map_viewer.html
- web_map_viewer.js

To view the generated web map, uou can now either copy your export folder to a web server, or use a simple web server (that supports http ranges). For example, on a system with NPM installed you can run in the export folder:

```npx http-server```

and view the output in a web browser at: http://127.0.0.1:8080/web_map_viewer.html

Alternatively, copy the [MapSplat](https://github.com/johnzastrow/mapsplat4) serve.py script to your export folder (a copy is available in plugin folder utilities/MapSplat) and run it with:

```
python serve.py (Windows)
python3 serve.py (macOS/Linux)
```
and view the output in a web browser at: http://127.0.0.1:8000/web_map_viewer.html

## Acknowledgements

_TBD (including SLDReader, MapSplat, qgis2web, Plugin Builder... and GitHub Copilot)_

## Your Feedback

If you come across bugs, please check first to see if it is already listed on the **Detailed Status and Viability Notes** (Link TBD) page, but if not please add a new issue.

At this proof of concept stage, please don't raise issue tickets for missing features - there are lots of things needed for a real plugin product, but I'm trying to focus on viability at the moment.

_TBD: come up with a better solution for more discursive feedback_