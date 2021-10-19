from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
from django.shortcuts import render, redirect
import json
from .forms import UserForm

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

@api_view(['GET', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')

def createAccount(request):

    form = UserForm()

    if request.method == 'POST':
        # print('Printing POST: ' , request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #<- saves in the database
            return redirect('/home/')


    context = {'form': form}
    return render(request, 'createAccount.html', context)


def home(request):
    return render(request, 'home.html')

def addItems(request):
    return render(request, 'addItems.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def userProfile(request):
    return render(request, 'userProfile.html')
