from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwrd = request.POST.get("pass")

        checkuser = authenticate(username = username, password = passwrd)

        if checkuser is not None:
            login(request, checkuser)
            return redirect("home")


    return render(request, "auth/loginpage.html")

def signuppage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        passsword = request.POST.get("pass")

        newuser = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = passsword)
        newuser.save()

    return render(request, "auth/signuppage.html")