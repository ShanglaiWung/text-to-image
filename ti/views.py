from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def renderHome(request):
    return render(request, 'ai-generator.html')


def renderAbout(request):
    return render(request, 'about.html')


def renderServices(request):
    return render(request, 'services.html')


def renderContactUs(request):
    return render(request, 'contact-us.html')
