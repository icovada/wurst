from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from wurst.num2name.models import Directory
from wurst.libs.xacmlparser import baseparser as baseparser

# Create your views here.
@csrf_exempt
def speeddial(request):
    if request.method == 'POST':

        calldata = baseparser(request.body)

        try:
            speedy = Directory.objects.get(speeddial=calldata['callednumber'])
        except ObjectDoesNotExist:
            return render(request, "nochange.xml")

        data = {'calledname': speedy.name,
                'callednumber': speedy.number}
        return render(request, "speeddialresponse.xml", data)
    elif request.method == 'HEAD':
        return HttpResponse()
    else:
        return HttpResponseForbidden("You must send data with POST method")