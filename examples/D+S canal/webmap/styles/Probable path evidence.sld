<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.1.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd">
 <NamedLayer>
  <se:Name>Probable path evidence</se:Name>
  <UserStyle>
   <se:Name>Probable path evidence</se:Name>
   <se:FeatureTypeStyle>
    <se:Rule>
     <se:Name>(Possible link)</se:Name>
     <se:Description>
      <se:Title>(Possible link)</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Confidence</ogc:PropertyName>
       <ogc:Literal>0</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#84d9ff</se:SvgParameter>
       <se:SvgParameter name="stroke-width">3</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">1 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Possible path (if built)</se:Name>
     <se:Description>
      <se:Title>Possible path (if built)</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsEqualTo>
       <ogc:PropertyName>Confidence</ogc:PropertyName>
       <ogc:Literal>1</ogc:Literal>
      </ogc:PropertyIsEqualTo>
     </ogc:Filter>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#84d9ff</se:SvgParameter>
       <se:SvgParameter name="stroke-width">3</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">4 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:Name>Probable path</se:Name>
     <se:Description>
      <se:Title>Probable path</se:Title>
     </se:Description>
     <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
      <ogc:PropertyIsGreaterThan>
       <ogc:PropertyName>Confidence</ogc:PropertyName>
       <ogc:Literal>1</ogc:Literal>
      </ogc:PropertyIsGreaterThan>
     </ogc:Filter>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#e24646</se:SvgParameter>
       <se:SvgParameter name="stroke-width">3</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
     <se:LineSymbolizer>
      <se:Stroke>
       <se:SvgParameter name="stroke">#84d9ff</se:SvgParameter>
       <se:SvgParameter name="stroke-width">3</se:SvgParameter>
       <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
       <se:SvgParameter name="stroke-linecap">butt</se:SvgParameter>
       <se:SvgParameter name="stroke-dasharray">4 2</se:SvgParameter>
      </se:Stroke>
     </se:LineSymbolizer>
    </se:Rule>
    <se:Rule>
     <se:MinScaleDenominator>1</se:MinScaleDenominator>
     <se:MaxScaleDenominator>5000</se:MaxScaleDenominator>
     <se:TextSymbolizer>
      <se:Label>
       <ogc:PropertyName>ID</ogc:PropertyName>
      </se:Label>
      <se:Font>
       <se:SvgParameter name="font-family">Arial</se:SvgParameter>
       <se:SvgParameter name="font-size">10</se:SvgParameter>
      </se:Font>
      <se:LabelPlacement>
       <se:LinePlacement>
        <se:GeneralizeLine>true</se:GeneralizeLine>
       </se:LinePlacement>
      </se:LabelPlacement>
      <se:Halo>
       <se:Radius>2</se:Radius>
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
