from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def renderHome():
    return HttpResponse('Hello')