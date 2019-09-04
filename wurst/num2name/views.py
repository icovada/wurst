from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from wurst.num2name.models import Directory
from wurst.libs.xacmlparser import baseparser as baseparser

# Create your views here.
@csrf_exempt
def num2name(request):
    if request.method == 'POST':

        calldata = baseparser(request.body)

        try:
            caller = Directory.objects.get(number=calldata['callingnumber'])
        except ObjectDoesNotExist:
            return render(request, "nochange.xml")

        data = {'callingname': caller.name}
        return render(request, "changecaller.xml", data)
    else:
        return HttpResponseForbidden("You must send data with POST method")