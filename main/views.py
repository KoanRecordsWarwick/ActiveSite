from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from main.models import *

def index(request):
    carousel = Carousel.objects.get(name='index'),
    c = {
            "images" : carousel[0].images.all()
        }
    return render(request, 'index.html', c)

def news(request):
    return render(request, 'news.html')

def artists(request):
    return render(request, 'artists.html')

def releases(request):
    c = {
            "videos" : Release.objects.filter(typevideotrack='video'),
            "tracks" : Release.objects.filter(typevideotrack='track'),
        }
    return render(request, 'releases.html', c)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def test(request):
    return HttpResponse("Hello World")

# Create your views here.
