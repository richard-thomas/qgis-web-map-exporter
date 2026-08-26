<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>Notable features (SVG Marker)</se:Name>
  <UserStyle>
   <se:Name>Notable features (SVG Marker)</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>Single symbol</se:Name>
     <se:PointSymbolizer>
      <se:Graphic>
       <!--Parametric SVG-->
       <se:ExternalGraphic>
        <se:OnlineResource xlink:href="https://raw.githubusercontent.com/qgis/QGIS/refs/heads/master/images/svg/symbol/red-marker.svg?fill=%23232323&amp;fill-opacity=1&amp;outline=%23232323&amp;outline-opacity=1&amp;outline-width=1" xlink:type="simple"/>
        <se:Format>image/svg+xml</se:Format>
       </se:ExternalGraphic>
       <!--Plain SVG fallback, no parameters-->
       <se:ExternalGraphic>
        <se:OnlineResource xlink:href="symbol/red-marker.svg" xlink:type="simple"/>
        <se:Format>image/svg+xml</se:Format>
       </se:ExternalGraphic>
       <!--Well known marker fallback-->
       <se:Mark>
        <se:WellKnownName>square</se:WellKnownName>
        <se:Fill>
         <se:SvgParameter name="fill">#232323</se:SvgParameter>
        </se:Fill>
        <se:Stroke>
         <se:SvgParameter name="stroke">#232323</se:SvgParameter>
         <se:SvgParameter name="stroke-width">1</se:SvgParameter>
        </se:Stroke>
       </se:Mark>
       <se:Size>34</se:Size>
       <se:Displacement>
        <se:DisplacementX>0</se:DisplacementX>
        <se:DisplacementY>-17</se:DisplacementY>
       </se:Displacement>
      </se:Graphic>
     </se:PointSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:TextSymbolizer>
      <se:Label>
       <ogc:PropertyName>title</ogc:PropertyName>
      </se:Label>
      <se:Font>
       <se:SvgParameter name="font-family">Arial</se:SvgParameter>
       <se:SvgParameter name="font-size">13</se:SvgParameter>
      </se:Font>
      <se:LabelPlacement>
       <se:PointPlacement>
        <se:AnchorPoint>
         <se:AnchorPointX>0.5</se:AnchorPointX>
         <se:AnchorPointY>1</se:AnchorPointY>
        </se:AnchorPoint>
        <se:Displacement>
         <se:DisplacementX>0</se:DisplacementX>
         <se:DisplacementY>3</se:DisplacementY>
        </se:Displacement>
       </se:PointPlacement>
      </se:LabelPlacement>
      <se:Halo>
       <se:Radius>1</se:Radius>
       <se:Fill>
        <se:SvgParameter name="fill">#ffffff</se:SvgParameter>
       </se:Fill>
      </se:Halo>
      <se:Fill>
       <se:SvgParameter name="fill">#000000</se:SvgParameter>
      </se:Fill>
     </se:TextSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
