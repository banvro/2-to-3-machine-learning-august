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
    all_Data = Contactus.objects.all().order_by("-id")
    seriliz_data = contactusserlizer(all_Data, many = True)
    return Response({"message" : "data fetch Sucessfully", "data" : seriliz_data.data})


@api_view(["POST"])
def savingdata(request):
    # print(request.data)
    serlizer = contactusserlizer(data = request.data)
    if serlizer.is_valid():
        serlizer.save()
        return Response({"Message" : "Data Saved Successfuly..", "status" : "Done", "data" : serlizer.data})
    else:
        return Response({"Message" : "Data Not Saved", "status" : "Not Done", "error" : "Enter all fields"})
    

@api_view(["DELETE"])
def deletedata(request, id):
    if Contactus.objects.filter(id = id):
        record = Contactus.objects.get(id = id)
        record.delete()
        return Response({"message" : "Data Deleted", "stsus" : "done", "your_is" : id})
    else:
        return Response({"Message" : "Data not found", "status" : "Not Done"})


@api_view(["PATCH"])
def updatedata(request, id):
    record = Contactus.objects.get(id = id)
    serizer = contactusserlizer(record, data = request.data,  partial = True)

    try:
        if serizer.is_valid():
            serizer.save()
            return Response({"Messafe" : "Data Updated Successfully", "Status" : "Done"})
        else:
                return Response({"Message" : "Data not found", "status" : "Not Done"})
    except Exception as e:
        return Response({"Message" : e})