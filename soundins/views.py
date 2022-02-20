from django.shortcuts import render
 
from .models import Instrument

# Create your views here.


def index(request):
    return render(request, "soundins/index.html",{
        "allIns":Instrument.objects.all()
    })