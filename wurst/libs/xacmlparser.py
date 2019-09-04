import xml.etree.ElementTree as ET

def baseparser(data):
    root = ET.fromstring(data)

    for element in root.getchildren():
        if element.tag == '{urn:oasis:names:tc:xacml:2.0:context:schema:os}Subject':
            subject = element

            calldata = {}

            for element in subject:
                name = element.attrib.get('AttributeId')
                if "urn:Cisco:uc:1.0:" in name:
                    value = str(element.getchildren()[0].text)
                    calldata[name[17:]] = value

    return calldata
        