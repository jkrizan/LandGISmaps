# -*- coding: utf-8 -*-

def get_href(layer_name):
    wmskml_url = 'https://geoserver.opengeohub.org/landgisgeoserver/wms/kml?layers={}'.format(layer_name)
    
    wmskml_txt = requests.get(wmskml_url).text
    wmskml_xml = minidom.parseString(wmskml_txt)
    
    href_node = wmskml_xml.getElementsByTagName('href')
    if len(href_node)>0:
        href = href_node[0].childNodes[0].nodeValue
        return href
    else:
        exception_node = wmskml_xml.getElementsByTagName('ServiceException')
        if len(exception_node)>0:
            err = exception_node[0].childNodes[0].nodeValue
        else:
            err = "Unknown error while fetching network link for {}".format(layer_name)
            
        raise Exception("get_href: " + err)