from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse("this is home page")
    return render(request, "home.html")

def aboutus(request):
    # return HttpResponse("this is about us page")
    return render(request, "about.html")


# Blog 

# home 
# about
# contact us 
# services