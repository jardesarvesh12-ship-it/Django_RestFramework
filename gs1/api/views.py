from django.shortcuts import render

# Create your views here.

from .models import Student                      # imports Student model from models.py.
from .serializers import StudentSerializer, StudentModelSerializer      # Serializer converts: Model Object → Python Dict , Python Dict → JSON
from rest_framework.renderers import JSONRenderer # JSONRenderer converts Python dict data into JSON format.
from django.http import HttpResponse     # Used to send response back to browser/client.


# 1. This Function is used to get single student data from database based on id (primary key) and send it to frontend.
def student_detail(request , pk):
    stu = Student.objects.get(id=pk)        # Get Data From Database
    serializer = StudentSerializer(stu)     # Converts model object into Python dictionary.
    json_data = JSONRenderer().render(serializer.data)  # Convert Python Data to JSON
    return HttpResponse(json_data, content_type = "application/json") # Return JSON Response


# 2. This Function is used to get multiple students data from database and send it to frontend.
def student_list(request):
    stu = Student.objects.all()                # Get Data From Database
    serializer = StudentModelSerializer(stu, many = True) # Converts model object into Python dictionary.
    json_data = JSONRenderer().render(serializer.data)  # Convert Python Data to JSON
    return HttpResponse(json_data, content_type = "application/json") # Return JSON Response
