from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapis.models import Contactus
from myapis.serilizer import contactusserlizer

# JSON --> data structue 
# json --> (Javascript object notation)

# Create your views here.

@api_view(["GET", "POST"])
def myfirstapi(request):
    return Response({"message" : "this is my first API", "Status" : "Done"})



@api_view(["GET"])
def getingdata(request):
    all_Data = Contactus.objects.all()
    seriliz_data = contactusserlizer(all_Data, many = True)
    return Response({"message" : "data fetch Sucessfully", "data" : seriliz_data.data})


