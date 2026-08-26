<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>Allotment sites</se:Name>
  <UserStyle>
   <se:Name>Allotment sites</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>Redland Green Allotments</se:Name>
     <se:Description>
      <se:Title>Redland Green Allotments</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>SITE_NAME</ogc:PropertyName>
       <ogc:Literal>Redland Green Allotments</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:GraphicFill>
        <se:Graphic>
         <se:Mark>
          <se:WellKnownName>x</se:WellKnownName>
          <se:Stroke>
           <se:SvgParameter name="stroke">#3f6cd6</se:SvgParameter>
           <se:SvgParameter name="stroke-opacity">0.28</se:SvgParameter>
          </se:Stroke>
         </se:Mark>
        </se:Graphic>
       </se:GraphicFill>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#232323</se:SvgParameter>
       <se:SvgParameter name="stroke-opacity">0.11</se:SvgParameter>
       <se:SvgParameter name="stroke-width">4</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">4 2</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Metford Road Allotments</se:Name>
     <se:Description>
      <se:Title>Metford Road Allotments</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>SITE_NAME</ogc:PropertyName>
       <ogc:Literal>Metford Road Allotments</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#9d3cc0</se:SvgParameter>
       <se:SvgParameter name="stroke-opacity">0.35</se:SvgParameter>
       <se:SvgParameter name="stroke-width">4</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">7 7</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
