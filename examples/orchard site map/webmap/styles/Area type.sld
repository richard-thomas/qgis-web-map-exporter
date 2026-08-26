<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>Area type</se:Name>
  <UserStyle>
   <se:Name>Area type</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>Open Area</se:Name>
     <se:Description>
      <se:Title>Open Area</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Open Area</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#aaf4aa</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.68</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#afb38a</se:SvgParameter>
       <se:SvgParameter name="stroke-opacity">0</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <!--Parametric SVG-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/landuse_grass.svg?fill=%2323c823&amp;fill-opacity=0.57&amp;outline=%2323c823&amp;outline-opacity=1&amp;outline-width=1" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Plain SVG fallback, no parameters-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="symbol/landuse_grass.svg" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Well known marker fallback-->
         <se:Mark>
          <se:WellKnownName>square</se:WellKnownName>
          <se:Fill>
           <se:SvgParameter name="fill">#23c823</se:SvgParameter>
           <se:SvgParameter name="fill-opacity">0.57</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
           <se:SvgParameter name="stroke">#23c823</se:SvgParameter>
           <se:SvgParameter name="stroke-width">1</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
         <se:Size>43</se:Size>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
     </se:PolygonSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Wildflowers</se:Name>
     <se:Description>
      <se:Title>Wildflowers</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Wildflowers</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#f1f4c7</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#afb38a</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <!--Parametric SVG-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/landuse_scrub.svg?fill=%23d8dca0&amp;fill-opacity=1&amp;outline=%2382846c&amp;outline-opacity=1&amp;outline-width=1" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Plain SVG fallback, no parameters-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="symbol/landuse_scrub.svg" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Well known marker fallback-->
         <se:Mark>
          <se:WellKnownName>square</se:WellKnownName>
          <se:Fill>
           <se:SvgParameter name="fill">#d8dca0</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
           <se:SvgParameter name="stroke">#82846c</se:SvgParameter>
           <se:SvgParameter name="stroke-width">1</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
         <se:Size>43</se:Size>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
     </se:PolygonSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Growing Area</se:Name>
     <se:Description>
      <se:Title>Growing Area</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Growing Area</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#badd69</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#809848</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <!--Parametric SVG-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/landuse_quary.svg?fill=%2364b364&amp;fill-opacity=1&amp;outline=%23335e33&amp;outline-opacity=1&amp;outline-width=1" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Plain SVG fallback, no parameters-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="symbol/landuse_quary.svg" xlink:type="simple"/>
          <se:Format>image/svg+xml</se:Format>
         </se:ExternalGraphic>
         <!--Well known marker fallback-->
         <se:Mark>
          <se:WellKnownName>square</se:WellKnownName>
          <se:Fill>
           <se:SvgParameter name="fill">#64b364</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
           <se:SvgParameter name="stroke">#335e33</se:SvgParameter>
           <se:SvgParameter name="stroke-width">1</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
         <se:Size>21</se:Size>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
     </se:PolygonSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Dead Hedge</se:Name>
     <se:Description>
      <se:Title>Dead Hedge</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Dead Hedge</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#a77f4d</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.39</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-opacity">0.61</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Hugelkultur Bed</se:Name>
     <se:Description>
      <se:Title>Hugelkultur Bed</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Hugelkultur Bed</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#bc6591</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.39</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-opacity">0.61</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Silt Beds</se:Name>
     <se:Description>
      <se:Title>Silt Beds</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Silt Beds</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#9caa65</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.68</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <!--Parametric SVG-->
         <se:ExternalGraphic>
          <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/landuse_swamp.svg?fill=%239bbd65&amp;fill-opacity=0.57&amp;outline=%23575c00&amp;outline-opacity=0.68&amp;outline-width=1" xlink:type="simple"/>
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
           <se:SvgParameter name="fill">#9bbd65</se:SvgParameter>
           <se:SvgParameter name="fill-opacity">0.57</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
           <se:SvgParameter name="stroke">#575c00</se:SvgParameter>
           <se:SvgParameter name="stroke-opacity">0.68</se:SvgParameter>
           <se:SvgParameter name="stroke-width">1</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
         <se:Size>36</se:Size>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:MinScaleDenominator>1</se:MinScaleDenominator>
     <se:MaxScaleDenominator>250</se:MaxScaleDenominator>
     <se:TextSymbolizer>
      <se:Label>
       <ogc:PropertyName>label</ogc:PropertyName>
      </se:Label>
      <se:Font>
       <se:SvgParameter name="font-family">Arial</se:SvgParameter>
       <se:SvgParameter name="font-size">14</se:SvgParameter>
      </se:Font>
      <se:LabelPlacement>
       <se:PointPlacement>
        <se:AnchorPoint>
         <se:AnchorPointX>0.5</se:AnchorPointX>
         <se:AnchorPointY>0.5</se:AnchorPointY>
        </se:AnchorPoint>
       </se:PointPlacement>
      </se:LabelPlacement>
      <se:Fill>
       <se:SvgParameter name="fill">#000000</se:SvgParameter>
      </se:Fill>
     </se:TextSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
