from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show(response,*args,**kwargs):
    return HttpResponse("hello_world. I fuck prostitutes nowadays. And it is good!")