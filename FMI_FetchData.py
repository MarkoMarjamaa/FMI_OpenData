
import sys
import datetime
import urllib2
import lxml.etree as etree
from datetime import date, timedelta

strApiKey = sys.argv[1]
strUrlStart = "http://data.fmi.fi/fmi-apikey/"

# Station id
LOC_MAJAKKA = "101003"
LOC_AALTO   = "134221"
LOC_PORVOO  = "101022"
	
for year in range(2013, 2004,-1) :
	nDays = (datetime.datetime(year, 12, 31)-datetime.datetime(year, 1, 1)).days+1
#	print  "Days: "+ str(nDays)
	for iDay in range (nDays,0,-7) :
		iStart = iDay
		iEnd = iDay+6
		if iStart <= nDays : 
			if iEnd > nDays :
				iEnd = nDays
				
			dateStart = datetime.datetime.strptime(str(year) + " " + str(iStart)  , '%Y %j')
			dateEnd = datetime.datetime.strptime(str(year) + " " + str(iEnd)  , '%Y %j')
			strStartTime = dateStart.strftime('%Y-%m-%dT00:00:00Z')
			strEndTime = dateEnd.strftime('%Y-%m-%dT23:59:59Z')
			print "Viikko : " + strStartTime + " " + strEndTime

			# Fetch wave buoy from Suomenlahti 
			strUrl = strUrlStart + strApiKey + "/wfs?request=getFeature&storedquery_id=fmi::observations::wave::timevaluepair&fmisid=" + LOC_AALTO + "&starttime=" + strStartTime + "&endtime=" + strEndTime  

			strXMLResult = urllib2.urlopen(strUrl).read()
			xmlResult = etree.XML(strXMLResult)

			# Read XSLT File
			strXSLTFilename = "FMI_WaveData.xslt"
			xmlXsltRoot = etree.parse(strXSLTFilename)
			xmlXSLT = etree.XSLT(xmlXsltRoot)

			# Transform with XSLT
			xmlDest = xmlXSLT(xmlResult)

			# print xmlDest
			myFile = open("Aalto_" + dateStart.strftime('%Y%m%d') + ".csv", 'w')
			myFile.write(str(xmlDest))
			myFile.close()

			# Fetch Majakka
			strUrl = strUrlStart + strApiKey + "/wfs?request=getFeature&storedquery_id=fmi::observations::weather::timevaluepair&parameters=windspeedms,temperature&fmisid=" + LOC_MAJAKKA + "&starttime=" + strStartTime + "&endtime=" + strEndTime  

			strXMLResult = urllib2.urlopen(strUrl).read()
			xmlResult = etree.XML(strXMLResult)

			# Read XSLT File
			strXSLTFilename = "FMI_WindData.xslt"
			xmlXsltRoot = etree.parse(strXSLTFilename)
			xmlXSLT = etree.XSLT(xmlXsltRoot)

			# Transform with XSLT
			xmlDest = xmlXSLT(xmlResult)

			# print xmlDest
			myFile = open("Majakka_" + dateStart.strftime('%Y%m%d') + ".csv", 'w')
			myFile.write(str(xmlDest))
			myFile.close()

			# Fetch Porvoo
			strUrl = strUrlStart + strApiKey + "/wfs?request=getFeature&storedquery_id=fmi::observations::weather::timevaluepair&parameters=windspeedms,temperature&fmisid=" + LOC_PORVOO + "&starttime=" + strStartTime + "&endtime=" + strEndTime  

			strXMLResult = urllib2.urlopen(strUrl).read()
			xmlResult = etree.XML(strXMLResult)

			# Read XSLT File
			strXSLTFilename = "FMI_WindData.xslt"
			xmlXsltRoot = etree.parse(strXSLTFilename)
			xmlXSLT = etree.XSLT(xmlXsltRoot)

			# Transform with XSLT
			xmlDest = xmlXSLT(xmlResult)

			# print xmlDest
			myFile = open("Porvoo_" + dateStart.strftime('%Y%m%d') + ".csv", 'w')
			myFile.write(str(xmlDest))
			myFile.close()
