from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def articles(request):
    return HttpResponse("Hello, welcome to the Articles page") 
