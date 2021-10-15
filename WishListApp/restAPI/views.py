from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .serializer import ItemSerializer
from .serializer import WishListSerializer
from .models import User
from .models import Item
from .models import Wishlist
import json

from rest_framework.decorators import api_view

from django.shortcuts import render
from django.urls import path
from . import views


@api_view(['GET'])
def items_list(request, uId):
    if request.method == 'GET':
        wList = Wishlist.objects.filter(userid=uId)
        serializer1 = WishListSerializer(wList, many=True)
        json1 = json.dumps(serializer1.data)
        print("Wishlists:\n", json1)
        return Response(serializer1.data)


@api_view(['GET'])
def users_list(request):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def user_detail(request, uName):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user = User.objects.get(username=uName)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
