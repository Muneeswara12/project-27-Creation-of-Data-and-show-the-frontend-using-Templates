from django.shortcuts import render

from app.models import *

# Create your views here.

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def webpages(request):
    LWO=Webpage.objects.all()
    d={'webpages':LWO}
    return render(request,'webpages.html',d)

def accessrecords(request):
    accessrecords=AccessRecords.objects.all()
    d={'accessrecords':accessrecords}
    return render(request,'accessrecords.html',d)