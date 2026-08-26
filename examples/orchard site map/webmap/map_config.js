var mapConfig = {
    "pageTitle": "Orchard Site Map",
    "displayProjection": "EPSG:3857",
    "initialMapExtent": [
        -290298.3063910783,
        6705611.658595271,
        -289635.87301732216,
        6705883.1719613
    ],
    "dataLayersConfig": [
        {
            "data_url": "data/Zone labels.geojson",
            "label": "Zone labels",
            "style": "styles/Zone labels.sld",
            "z_index": -1
        },
        {
            "data_url": "data/Other plants.fgb",
            "label": "Other plants",
            "style": "styles/Other plants.sld",
            "z_index": -2
        },
        {
            "data_url": "data/Steps.fgb",
            "label": "Steps",
            "style": "styles/Steps.sld",
            "z_index": -3
        },
        {
            "data_url": "data/Fruit trees.geojson",
            "label": "Fruit trees",
            "style": "styles/Fruit trees.sld",
            "z_index": -4
        },
        {
            "data_url": "data/Other trees or shrubs.geojson",
            "label": "Other trees or shrubs",
            "style": "styles/Other trees or shrubs.sld",
            "z_index": -5
        },
        {
            "data_url": "data/Pre-hedgelaying other trees.geojson",
            "label": "Pre-hedgelaying other trees",
            "style": "styles/Pre-hedgelaying other trees.sld",
            "z_index": -6
        },
        {
            "data_url": "data/Soft fruits.geojson",
            "label": "Soft fruits",
            "style": "styles/Soft fruits.sld",
            "z_index": -7
        },
        {
            "data_url": "data/Infrastructure.fgb",
            "label": "Infrastructure",
            "style": "styles/Infrastructure.sld",
            "z_index": -8
        },
        {
            "data_url": "data/Barriers.fgb",
            "label": "Barriers",
            "style": "styles/Barriers.sld",
            "z_index": -9
        },
        {
            "data_url": "data/Water features.fgb",
            "label": "Water features",
            "style": "styles/Water features.sld",
            "z_index": -10
        },
        {
            "data_url": "data/Footpaths.pmtiles",
            "label": "Footpaths",
            "style": "styles/Footpaths.sld",
            "z_index": -11
        },
        {
            "data_url": "data/Area_type.pmtiles",
            "label": "Area type",
            "style": "styles/Area type.sld",
            "z_index": -12
        },
        {
            "data_url": "data/Allotment plots.fgb",
            "label": "Allotment plots",
            "style": "styles/Allotment plots.sld",
            "z_index": -13
        },
        {
            "data_url": "data/Allotment sites.fgb",
            "label": "Allotment sites",
            "style": "styles/Allotment sites.sld",
            "z_index": -14
        }
    ]
};
