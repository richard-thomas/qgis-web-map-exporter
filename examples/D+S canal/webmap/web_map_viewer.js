// Template for loading a web map from the 'Web Map Exporter' QGIS plugin.
// Note: The hosting server MUST support HTTP Range Requests and CORS.

// Set source loading strategy to either loading all at once or bounding box that is current view
//const loadingStrategy = (extent) => [[-Infinity, -Infinity, Infinity, Infinity]];
const loadingStrategy = (extent) => [extent];

// Get some custom settings from map_config.js
const displayProjection = mapConfig.displayProjection;
const initialMapExtent = mapConfig.initialMapExtent;
document.title = mapConfig.pageTitle;

// Check if we need to add Proj4s definition for requested display projection
if (!ol.proj.get(mapConfig.displayProjection)) {
    const proj4String = mapConfig.proj4String;
    if (typeof proj4 === "undefined") {
        console.error("Cannot add the missing requested display projection [" +
        displayProjection + "] because the Proj4js library has not been loaded");
    }
    //console.log("INFO: adding missing requested display projection [" +
    //    displayProjection + "] with Proj4s string:\n" + proj4String);
    proj4.defs(displayProjection, proj4String);
    ol.proj.proj4.register(proj4);
}

// Example hard-wired base layer
// For dev, can disable/adjust dynamically in browser developer tools console:
//   osm_greyscale_lyr.setOpacity(0)
window.osm_greyscale_lyr = new ol.layer.Tile({
    source: new ol.source.OSM(),
    zIndex: -1000,
    opacity: 0.3,
    className: 'ol-grayscale'
});

// Create map with various controls and an example OpenStreetMap baselayer
const map = new ol.Map({
    target: 'map',
    layers: [
        //osm_greyscale_lyr
    ],
    view: new ol.View({
        projection: displayProjection
    }),
    controls: ol.control.defaults.defaults().extend([
        new ol.control.ZoomToExtent({
            extent: initialMapExtent,
        }),
        new ol.control.FullScreen(),
        new ol.control.MousePosition({
            coordinateFormat: ol.coordinate.createStringXY(4),
            projection: 'EPSG:4326'
        }),
        new ol.control.ZoomSlider()
    ])
});
map.getView().fit(initialMapExtent, {
    size: map.getSize(),
    padding: [10, 10, 10, 10]
})

// Load data layers and styles defined in map_config.js
const dataLayersConfig = mapConfig.dataLayersConfig;
let dataLayerList = [];
for (const layer of dataLayersConfig) {
    let vectorLayer;
    const dataUrl = layer.data_url
    if (dataUrl === '') {
        console.warn(`Skipping layer "${layer.label}" - no source data available!`);
        continue;
    }

    // FlatGeoBuf data source
    if (dataUrl.endsWith('.fgb')) {
        const vectorSource = new ol.source.Vector({ strategy: loadingStrategy });
        const loader = flatgeobuf.createLoader(vectorSource, dataUrl, displayProjection, loadingStrategy, false)
        vectorSource.setLoader(loader);
        vectorLayer = new ol.layer.Vector({ source: vectorSource });

    // PMTiles (vector) tile data source
    // TBD: handle PMTiles raster sources which also end .pmtiles
    } else if (dataUrl.endsWith('.pmtiles')) {
        vectorLayer = new ol.layer.VectorTile({
            source: new olpmtiles.PMTilesVectorSource({
                url: dataUrl,
                //projection: displayProjection
            }),
        });

    // GeoJSON data source
    } else if (dataUrl.endsWith('.geojson')) {
        vectorLayer = new ol.layer.Vector({
            source: new ol.source.Vector({
                url: dataUrl,
                format: new ol.format.GeoJSON()
            })
        });

    // GeoParquet data source
    } else if (dataUrl.endsWith('.parquet')) {
        // No native GeoParquet support in OpenLayers. As it is a columnar format,
        // ideally would want to only get geometry and any attributes required
        // for styling, with any selection popups fetching additional attributes on the fly.
        console.warn(`Discarding layer "${layer.label}": GeoParquet format currently unsupported`);
        continue

    // (Currently) unsupported data source
    } else {
        console.warn(`Layer "${layer.label}": Discarding unsupported type "${dataUrl}"`);
        continue
    }

    vectorLayer.set('title', layer.label);
    vectorLayer.set('zIndex', layer.z_index);
    dataLayerList.unshift(vectorLayer);

    // Apply vector layer styling from associated SLD file
    const sldUrl = layer.style;
    if (sldUrl !== '') {
        loadSldStyle(sldUrl, vectorLayer);
    } else {
        console.warn(`No SLD styling available for layer "${layer.label}"`)
    }
}

map.getLayers().extend(dataLayerList);

// Add layer selection control
var layerSwitcher = new ol.control.LayerSwitcher({
    groupSelectStyle: 'children' // Can be 'children' [default], 'group' or 'none'
});
map.addControl(layerSwitcher);

/**
 * Load styling for selected vector layer from SLD data
 * @param {string} sldUrl - URL of SLD file
 * @param {ol_layer_Vector} vectorLayer - existing OL Vector Layer
 */
async function loadSldStyle(sldUrl, vectorLayer) {
    try {
        const response = await fetch(sldUrl);
        const sldXml = await response.text();

        // Parse the SLD XML into an SLD object.
        const sldObject = SLDReader.Reader(sldXml, { compatibilityMode: 'QGIS' });
        //console.log(`SLD object for layer "${sldUrl}":`);
        //console.log(sldObject.layers[0]);

        // Use the first FeatureTypeStyle element in the SLD.
        const featureTypeStyle = sldObject.layers[0].styles[0].featuretypestyles[0];

        // Create a (feature -> [ol styles]) style function from the FeatureTypeStyle.
        const styleFunction = SLDReader.createOlStyleFunction(featureTypeStyle);

        vectorLayer.setStyle(styleFunction);
    } catch (error) {
        console.error(`Error occurred loading SLD file '${sldUrl}':\n  ${error}`);
    }
}
