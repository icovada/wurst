from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
import xml.etree.ElementTree as ET


# Create your views here.
@csrf_exempt
def num2name(request):
    if request.method == 'POST':
        tree = ET.parse(request.POST.get('data'))
        root = tree.getroot()

        for element in root.getchildren():
            if element.tag == '{urn:oasis:names:tc:xacml:2.0:context:schema:os}Subject':
                subject = element

        calldata = {}

        for element in subject:
            calldata[element.attrib.get('AttributeID')] = element
        
        

        return HttpResponse("Test")
    else:
        return HttpResponseForbidden("You must send data with POST method")