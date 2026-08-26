<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>OS 1st edition (SVG Fill)</se:Name>
  <UserStyle>
   <se:Name>OS 1st edition (SVG Fill)</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>Hachure</se:Name>
     <se:Description>
      <se:Title>Hachure</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Type</ogc:PropertyName>
       <ogc:Literal>Hachure</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>0</se:MinScaleDenominator>
     <se:MaxScaleDenominator>10000</se:MaxScaleDenominator>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#673f20</se:SvgParameter>
       <se:SvgParameter name="stroke-width">2.39999999999999991</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">0.3 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Infrastructure</se:Name>
     <se:Description>
      <se:Title>Infrastructure</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Type</ogc:PropertyName>
       <ogc:Literal>Infrastructure</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>0</se:MinScaleDenominator>
     <se:MaxScaleDenominator>10000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#d5b43c</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.49</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#8e7424</se:SvgParameter>
       <se:SvgParameter name="stroke-width">2</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Marsh</se:Name>
     <se:Description>
      <se:Title>Marsh</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Type</ogc:PropertyName>
       <ogc:Literal>Marsh</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>0</se:MinScaleDenominator>
     <se:MaxScaleDenominator>10000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <!--Parametric SVG-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/landuse_swamp.svg?fill=%23e5aa35&amp;fill-opacity=1&amp;outline=%23296e3a&amp;outline-opacity=1&amp;outline-width=1" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Plain SVG fallback, no parameters-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="symbol/landuse_swamp.svg" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Well known marker fallback-->
         <se:Mark>
          <se:WellKnownName>square</se:WellKnownName>
          <se:Fill>
           <se:SvgParameter name="fill">#e5aa35</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
           <se:SvgParameter name="stroke">#296e3a</se:SvgParameter>
           <se:SvgParameter name="stroke-width">1</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
         <se:Size>36</se:Size>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
     </se:PolygonSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#2aae2a</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#cab982</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.36</se:SvgParameter>
      </se:Fill>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Water</se:Name>
     <se:Description>
      <se:Title>Water</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Type</ogc:PropertyName>
       <ogc:Literal>Water</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>0</se:MinScaleDenominator>
     <se:MaxScaleDenominator>10000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#39e5e8</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.36</se:SvgParameter>
      </se:Fill>
     </se:PolygonSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#228b8f</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">1 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Enclosure boundary</se:Name>
     <se:Description>
      <se:Title>Enclosure boundary</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Type</ogc:PropertyName>
       <ogc:Literal>Enclosure boundary</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>0</se:MinScaleDenominator>
     <se:MaxScaleDenominator>10000</se:MaxScaleDenominator>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#ffa536</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">4 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
