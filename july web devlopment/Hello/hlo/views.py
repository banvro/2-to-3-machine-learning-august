from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contactus.html")

def servicespage(request):
    return render(request, "services.html")