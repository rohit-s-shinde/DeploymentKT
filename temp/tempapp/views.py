from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import time

@api_view(['GET'])
def hello(request):
    time.sleep(10)
    return Response({"Hello World!"}, status.HTTP_200_OK)

@api_view(['GET'])
def bye(request):
    return Response({"Good bye!"}, status.HTTP_200_OK)