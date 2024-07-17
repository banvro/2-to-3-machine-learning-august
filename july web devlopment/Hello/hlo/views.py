from django.shortcuts import render, redirect
from django.http import HttpResponse
from hlo.models import ContactUs
# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contactus.html")

def servicespage(request):
    return render(request, "services.html")


def savedata(request):
    if request.method == "POST":
        full_name = request.POST.get('fname')
        email = request.POST.get("email")
        phn_num = request.POST.get("pnumber")
        msg = request.POST.get("msg")

        # print(full_name, email, phn_num, msg)
        data = ContactUs(fullname = full_name, 
                         email = email, 
                         phone_number = phn_num,
                         message = msg)
        data.save()
        return redirect('contact')

    return HttpResponse("data saved sucessfully...!")