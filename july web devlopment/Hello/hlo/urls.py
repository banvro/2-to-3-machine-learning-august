from django.urls import path
from hlo import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("about", views.aboutus, name = "about")
]