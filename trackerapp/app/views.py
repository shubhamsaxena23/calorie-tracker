from django.shortcuts import render
from django.http import HttpResponse

def blah(request):
    return HttpResponse('blah')

def login(request):
    return render(request,"login.html")

# Create your views here.
