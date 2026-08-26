<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>Footpaths</se:Name>
  <UserStyle>
   <se:Name>Footpaths</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>Tarmac</se:Name>
     <se:Description>
      <se:Title>Tarmac</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>quality</ogc:PropertyName>
       <ogc:Literal>tarmac</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#807979</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#aca3a3</se:SvgParameter>
       <se:SvgParameter name="stroke-width">0.90000000000000002</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Patchy</se:Name>
     <se:Description>
      <se:Title>Patchy</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>quality</ogc:PropertyName>
       <ogc:Literal>patchy</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#eadede</se:SvgParameter>
       <se:SvgParameter name="stroke-width">0.85999999999999999</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">2 1</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Other</se:Name>
     <se:Description>
      <se:Title>Other</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:And>
       <ogc:PropertyIsNotEqualTo>
        <ogc:PropertyName>quality</ogc:PropertyName>
        <ogc:Literal>tarmac</ogc:Literal>
       </ogc:PropertyIsNotEqualTo>
       <ogc:PropertyIsNotEqualTo>
        <ogc:PropertyName>quality</ogc:PropertyName>
        <ogc:Literal>patchy</ogc:Literal>
       </ogc:PropertyIsNotEqualTo>
      </ogc:And>
     </ogc:Filter>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#beb4b4</se:SvgParameter>
       <se:SvgParameter name="stroke-width">1</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
     <se:LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
      <se:Stroke>
       <se:SvgParameter name="stroke">#eadede</se:SvgParameter>
       <se:SvgParameter name="stroke-width">0.90000000000000002</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">round</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
   </se:FeatureTypeStyle>
  </UserStyle>
 </NamedLayer>
</StyledLayerDescriptor>
