from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
import json

from rest_framework.decorators import api_view

from django.shortcuts import render
from django.urls import path
from . import views


@api_view(['GET'])
def users_list(request):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')

def createAccount(request):
    return render(request, 'createAccount.html')

def home(request):
    return render(request, 'home.html')

def addItems(request):
    return render(request, 'addItems.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def userProfile(request):
    return render(request, 'userProfile.html')
