from django.urls import path
from user import views

urlpatterns = [
    # path(url, view-funcation, name)
    path("home", views.homepage)
]