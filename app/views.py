from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>Hi girls missing your beautiful faces</h1></marquee>')
