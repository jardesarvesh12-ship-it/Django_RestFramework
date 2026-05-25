from django.contrib.sites import requests
from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser

from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.http import HttpResponse

from  django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):                             # this is my end-point to get data from database to frontend 
    if request.method == "GET":                        # GET is used to get data 
        json_data = request.body                        # get json data from frontend 
        stream = io.BytesIO(json_data)                  # convert python dict to stream
        pythondata = JSONParser().parse(stream)         # convert stream to python dict
        id = pythondata.get('id', None)                 # get id from python dict
        if id is not None:
            stu = Student.objects.get(id=id)                # get student data from database
            serializer = StudentSerializer(stu)             # serialize student data
            json_data = JSONRenderer().render(serializer.data)  # convert serialized data to json data
            return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend


        stu = Student.objects.all()                       # get all student data from database
        serializer = StudentSerializer(stu, many = True)    # serialize all student data
        json_data = JSONRenderer().render(serializer.data)  # convert serialized data to json data
        return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend


    #  For POST DATA INTO DATABASE 
    if request.method == "POST":
        json_data = request.body                       # get json data from frontend 
        stream = io.BytesIO(json_data)                   # convert python dict to stream
        pythondata = JSONParser().parse(stream)          # convert stream to python dict
        serializer = StudentSerializer(data = pythondata)  # create serializer instance with the data
        if serializer.is_valid():                        # check if the data is valid
            serializer.save()                            # save the data
            res = {'msg' : 'Data Created'}               # create response message 
            json_data = JSONRenderer().render(res)        # convert python dict to json data
            return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend
        json_data = JSONRenderer().render(serializer.errors)  # convert serialized data to json data
        return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend


# ====================>> Update DATA INTO DATABASE
    if request.method == "PUT":
        json_data = request.body                       # get json data from frontend 
        stream = io.BytesIO(json_data)                   # convert python dict to stream
        pythondata = JSONParser().parse(stream)          # convert stream to python dict
        id = pythondata.get('id', None)                  # get id from python dict
        stu = Student.objects.get(id=id)                 # get student data from database
        serializer = StudentSerializer(stu, data = pythondata)  # create serializer instance with the data
        if serializer.is_valid():                        # check if the data is valid
            serializer.save()                            # save the data
            res = {'msg' : 'Data Updated'}               # create response message 
            json_data = JSONRenderer().render(res)        # convert python dict to json data
            return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend
        json_data = JSONRenderer().render(serializer.errors)  # convert serialized data to json data
        return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend
        


# ====================>> Delete DATA INTO DATABASE

if request.method == "DELETE":
    json_data = request.body                         # get json data from frontend 
    stream = io.BytesIO(json_data)                   # convert python dict to stream
    pythondata = JSONParser().parse(stream)          # convert stream to python dict
    id = pythondata.get('id', None)                  # get id from python dict
    stu = Student.objects.get(id=id)                 # get student data from database
    stu.delete()                                     # delete student data
    res = {'msg' : 'Data Deleted'}                   # create response message 
    json_data = JSONRenderer().render(res)           # convert python dict to json data
    return HttpResponse(json_data, content_type = 'application/json')  # return json data to frontend