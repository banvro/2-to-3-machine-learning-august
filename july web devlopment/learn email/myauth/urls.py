from django.urls import path
from myauth import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about", views.about, name = "about"),
    path("login", views.loginpage, name = "loginpage"),
    path("signup", views.signuppage, name = "signuppage"),
    path("lets-logout", views.logutnow, name = "logout"),
    path("contact-us", views.contactus, name = "contact"),
   
]
