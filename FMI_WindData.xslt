<xsl:stylesheet version="2.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"

    xmlns:wfs="http://www.opengis.net/wfs/2.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:om="http://www.opengis.net/om/2.0"
    xmlns:omso="http://inspire.ec.europa.eu/schemas/omso/2.0rc3"
    xmlns:ompr="http://inspire.ec.europa.eu/schemas/ompr/2.0rc3"
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:gmd="http://www.isotc211.org/2005/gmd"
    xmlns:gco="http://www.isotc211.org/2005/gco"
    xmlns:swe="http://www.opengis.net/swe/2.0"
    xmlns:gmlcov="http://www.opengis.net/gmlcov/1.0"
    xmlns:sam="http://www.opengis.net/sampling/2.0"
    xmlns:sams="http://www.opengis.net/samplingSpatial/2.0"
    xmlns:wml2="http://www.opengis.net/waterml/2.0"
    xmlns:target="http://xml.fmi.fi/namespace/om/atmosphericfeatures/0.95"
	 >
	  <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
     <xsl:template match="/">

		<xsl:for-each select="/wfs:FeatureCollection/wfs:member/omso:PointTimeSeriesObservation/om:result/wml2:MeasurementTimeseries[@gml:id='obs-obs-1-1-windspeedms']/wml2:point/wml2:MeasurementTVP">  
			<xsl:variable name="time" select="./wml2:time/text()"/>
			<xsl:variable name="windspeedms" select="./wml2:value/text()"/>
			<xsl:for-each select="/wfs:FeatureCollection/wfs:member/omso:PointTimeSeriesObservation/om:result/wml2:MeasurementTimeseries[@gml:id='obs-obs-1-1-temperature']/wml2:point/wml2:MeasurementTVP[wml2:time=$time]">  
				<xsl:value-of select="$time"/><xsl:text>&#x9;</xsl:text>
				<xsl:value-of select="$windspeedms"/><xsl:text>&#x9;</xsl:text>
				<xsl:value-of select="./wml2:value/text()"/>
				<xsl:text>&#xa;</xsl:text>
			</xsl:for-each>
		</xsl:for-each>

     </xsl:template>
 </xsl:stylesheet>