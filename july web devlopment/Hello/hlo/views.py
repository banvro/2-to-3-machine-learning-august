from django.shortcuts import render, redirect
from django.http import HttpResponse
from hlo.models import ContactUs
# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    all_records = ContactUs.objects.all()
    # print(all_records)
    return render(request, "about.html", {"my_data" : all_records})

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
        img = request.FILES.get("myimg")

        # print(img, "xxxxxxxxxxxxxxxxxxx")
        print(full_name, email, phn_num, msg)
        data = ContactUs(fullname = full_name, 
                         email = email, 
                         phone_number = phn_num,
                         message = msg,
                         saveimg = img)
        data.save()
        return redirect('about')

    return HttpResponse("data saved sucessfully...!")


def deletedata(request, x):
    # print(x)
    rec = ContactUs.objects.get(id = x)
    rec.delete()
    return redirect("about")
    # return HttpResponse("data deleted sucessfully...!")


def updatedata(request, abc):
    obj = ContactUs.objects.get(id = abc)
    return render(request, "updatedata.html", {"record" : obj})


def updaterecord(request, abc):
    obj = ContactUs.objects.get(id = abc)
    if request.method == "POST":
        full_name = request.POST.get('fname')
        email = request.POST.get("email")
        phn_num = request.POST.get("pnumber")
        msg = request.POST.get("msg")

        # objectname.column_name = new_data
        obj.fullname = full_name
        obj.email = email
        obj.phone_number = phn_num
        obj.message = msg
        obj.save()

    return redirect("about")


def searching(request):
    query = request.GET.get("q")

    if query:
        xyz = ContactUs.objects.filter(email__icontains = query) | ContactUs.objects.filter(fullname__icontains = query) |ContactUs.objects.filter(phone_number__icontains = query)

        return render(request, "about.html", {"my_data" : xyz})
    else:
        all_records = ContactUs.objects.all()
        return render(request, "about.html", {"my_data" : all_records})