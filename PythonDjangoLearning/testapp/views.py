from django.shortcuts import render

# Create your views here.
def testapp(request):
    return render(request, "testapp/testapp_index.html")
