from django.urls import path
from myapis import views

urlpatterns = [
    path("first-api", views.myfirstapi, name = "firstapi"),
    path("get-data", views.getingdata, name = "get"),
    path("save-data", views.savingdata, name = "save"),
    path("delete-data/<int:id>", views.deletedata, name = "dlete"),
    path("update-data/<int:id>", views.updatedata, name = "udpate"),
]