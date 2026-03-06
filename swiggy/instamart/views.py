from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def icecream(request):
    return HttpResponse('<h1>I Love IceCreams </h1')