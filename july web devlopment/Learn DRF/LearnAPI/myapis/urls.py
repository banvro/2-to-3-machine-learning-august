from django.urls import path
from myapis import views

urlpatterns = [
    path("first-api", views.myfirstapi, name = "firstapi"),
    path("get-data", views.getingdata, name = "get"),
]