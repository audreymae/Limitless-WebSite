from django.shortcuts import render
from django.http import HttpResponse

# example2wdwaddsad
# Create your views here.


def articles(request):
    return HttpResponse("Hello, welcome to the Articles page") 
