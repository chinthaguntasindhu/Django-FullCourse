from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Biryani(request):
    return HttpResponse('<h1> Biryani is very tasty</h1>' )
