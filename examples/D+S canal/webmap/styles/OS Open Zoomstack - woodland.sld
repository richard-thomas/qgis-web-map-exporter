<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>OS Open Zoomstack - woodland</se:Name>
  <UserStyle>
   <se:Name>OS Open Zoomstack - woodland</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>National</se:Name>
     <se:Description>
      <se:Title>National</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>National</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>320000</se:MinScaleDenominator>
     <se:MaxScaleDenominator>2000000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#d1e7c3</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.5</se:SvgParameter>
      </se:Fill>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Regional</se:Name>
     <se:Description>
      <se:Title>Regional</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Regional</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>80000</se:MinScaleDenominator>
     <se:MaxScaleDenominator>320000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#d1e7c3</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.5</se:SvgParameter>
      </se:Fill>
     </se:PolygonSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Local</se:Name>
     <se:Description>
      <se:Title>Local</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>type</ogc:PropertyName>
       <ogc:Literal>Local</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:MinScaleDenominator>1</se:MinScaleDenominator>
     <se:MaxScaleDenominator>80000</se:MaxScaleDenominator>
     <se:PolygonSymbolizer>
      <se:Fill>
       <se:SvgParameter name="fill">#d1e7c3</se:SvgParameter>
       <se:SvgParameter name="fill-opacity">0.5</se:SvgParameter>
      </se:Fill>
      <se:Stroke>
       <se:SvgParameter name="stroke">#bacdae</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
      </se:Stroke>
     </se:PolygonSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
