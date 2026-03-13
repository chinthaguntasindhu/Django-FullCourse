from django.shortcuts import render

# Create your views here.
def listofbuses(request):
    return render(request,'listofbuses.html')

