from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Just a Home page | Landing page")
    return render(request, 'index.html') # or website/index.html if you choose to put you file in templates/website/

def about(request):
    return HttpResponse("About page")