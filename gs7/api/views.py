from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({'msg':"Hello World"})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#     return Response({'msg':"POST Request"})


# GET and POST data
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':"Hello World GET"})

    if request.method == 'POST':
        return Response({'msg':"Hello World POST"})
 