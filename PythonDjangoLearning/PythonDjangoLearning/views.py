from django.http import HttpResponse

def home(request):
    return HttpResponse("Just a Home page | Landing page")

def about(request):
    return HttpResponse("About page")