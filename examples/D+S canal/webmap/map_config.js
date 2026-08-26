var mapConfig = {
    "pageTitle": "D&S Canal",
    "displayProjection": "EPSG:3857",
    "initialMapExtent": [
        -279692.017174347,
        6660196.60640548,
        -256048.734179306,
        6668514.74116644
    ],
    "dataLayersConfig": [
        {
            "data_url": "data/Notable features (SVG Marker).geojson",
            "label": "Notable features (SVG Marker)",
            "style": "styles/Notable features (SVG Marker).sld",
            "z_index": -1
        },
        {
            "data_url": "data/Probable_path_evidence.pmtiles",
            "label": "Probable path evidence",
            "style": "styles/Probable path evidence.sld",
            "z_index": -3
        },
        {
            "data_url": "data/Probable_path_10m_nominal_width.pmtiles",
            "label": "Probable path (10m nominal width)",
            "style": "styles/Probable path (10m nominal width).sld",
            "z_index": -4
        },
        {
            "data_url": "data/Planned route (1796 Parliament Act map).fgb",
            "label": "Planned route (1796 Parliament Act map)",
            "style": "styles/Planned route (1796 Parliament Act map).sld",
            "z_index": -5
        },
        {
            "data_url": "data/Possible canal centreline.fgb",
            "label": "Possible canal centreline",
            "style": "styles/Possible canal centreline.sld",
            "z_index": -6
        },
        {
            "data_url": "data/Possible infrastructure.fgb",
            "label": "Possible infrastructure",
            "style": "styles/Possible infrastructure.sld",
            "z_index": -7
        },
        {
            "data_url": "data/1840s Tithe (boundary lines).fgb",
            "label": "1840s Tithe (boundary lines)",
            "style": "styles/1840s Tithe (boundary lines).sld",
            "z_index": -8
        },
        {
            "data_url": "data/1840s Tithe (canal).fgb",
            "label": "1840s Tithe (canal)",
            "style": "styles/1840s Tithe (canal).sld",
            "z_index": -9
        },
        {
            "data_url": "data/OS_1st_edition_SVG_Fill.pmtiles",
            "label": "OS 1st edition (SVG Fill)",
            "style": "styles/OS 1st edition (SVG Fill).sld",
            "z_index": -10
        },
        {
            "data_url": "data/Mapping extent.fgb",
            "label": "Mapping extent",
            "style": "styles/Mapping extent.sld",
            "z_index": -11
        },
        {
            "data_url": "data/Contour lines (10m) - OS Terrain 50.fgb",
            "label": "Contour lines (10m) - OS Terrain 50",
            "style": "styles/Contour lines (10m) - OS Terrain 50.sld",
            "z_index": -12
        },
        {
            "data_url": "data/OS Open Zoomstack - names.fgb",
            "label": "OS Open Zoomstack - names",
            "style": "styles/OS Open Zoomstack - names.sld",
            "z_index": -13
        },
        {
            "data_url": "data/OS Open Zoomstack - local buildings.fgb",
            "label": "OS Open Zoomstack - local buildings",
            "style": "styles/OS Open Zoomstack - local buildings.sld",
            "z_index": -14
        },
        {
            "data_url": "data/OS Open Zoomstack - surface water.fgb",
            "label": "OS Open Zoomstack - surface water",
            "style": "styles/OS Open Zoomstack - surface water.sld",
            "z_index": -15
        },
        {
            "data_url": "data/OS Open Zoomstack - woodland.fgb",
            "label": "OS Open Zoomstack - woodland",
            "style": "styles/OS Open Zoomstack - woodland.sld",
            "z_index": -16
        }
    ]
};
