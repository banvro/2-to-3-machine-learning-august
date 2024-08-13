from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myauth.models import UserCheck
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url="/login")
def home(request):
        user = User.objects.get(username = request.user)
        check_techer = UserCheck.objects.filter(userx = user).last()
        print(check_techer, "xxxxxxxxxxx")
        if check_techer:
            if check_techer.is_teacher:
                return render(request, "home.html")
            else:
                return HttpResponse("your are not authorize....")
        else:
            return HttpResponse("your are not authorize....")


@login_required(login_url="/login")
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

        checkdata = UserCheck(userx = newuser, is_teacher = True)
        checkdata.save()

    return render(request, "auth/signuppage.html")


def logutnow(request):
    logout(request)
    return redirect("home")