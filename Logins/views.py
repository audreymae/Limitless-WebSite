from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def logins(request):
    return HttpResponse("Hello, this will handle all the logins!") 
