from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from wurst.libs.models import Directory
from wurst.libs.xacmlparser import baseparser as baseparser

# Create your views here.
@csrf_exempt
def announcement(request):
    if request.method == 'POST':

        ann_id = request.GET['id']

        return render(request, "playannouncement.xml", {'ann_id': ann_id})
    elif request.method == 'HEAD':
        return HttpResponse()
    else:
        return HttpResponseForbidden("You must send data with POST method")