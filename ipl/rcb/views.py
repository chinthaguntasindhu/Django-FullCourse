from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1> Virat Kohil </h1')

def wisecaptain(request):
    return HttpResponse('<h1> Rajat Patidar </h1')

