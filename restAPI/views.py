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
#from .forms import UserForm

from rest_framework.decorators import api_view

from django.shortcuts import render, redirect
from django.urls import path
from . import views


@api_view(['GET', 'DELETE'])
def delete_item(request, iId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=iId)
        serializer = ItemSerializer(item, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        item = Item.objects.get(itemId=iId)
        item.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def wishlist_item_list(request, wId):
    if request.method == 'GET':
        wList = Wishlist.objects.filter(wishListId=wId)
        serializer1 = WishListSerializer(wList, many=True)
        json1 = json.loads(json.dumps(serializer1.data))
        print("Specific items from wishlist:", wId, "\n", json1)
        item_id_list = []
        for obj in json1:
            print(obj["itemId"])
            item_id_list.append(obj["itemId"])

        data_obj = []
        for id in item_id_list:
            temp_Item = Item.objects.get(itemId=id)
            temp_serializer = ItemSerializer(temp_Item, many=False)
            temp_json = json.loads(json.dumps(temp_serializer.data))
            print(temp_json)
            data_obj.append(temp_json)
        return Response(data_obj)


@api_view(['GET'])
def items_list(request, uId):
    if request.method == 'GET':
        wList = Wishlist.objects.filter(userid=uId)
        serializer1 = WishListSerializer(wList, many=True)
        json1 = json.loads(json.dumps(serializer1.data))
        print("Wishlists:\n", json1)
        print("Dictionary:")
        item_id_list = []
        for obj in json1:
            print(obj["itemId"])
            item_id_list.append(obj["itemId"])

        data_obj = []
        for id in item_id_list:
            temp_Item = Item.objects.get(itemId=id)
            temp_serializer = ItemSerializer(temp_Item, many=False)
            temp_json = json.loads(json.dumps(temp_serializer.data))
            print(temp_json)
            data_obj.append(temp_json)
        return Response(data_obj)


@api_view(['GET'])
def users_list(request):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        print("******")
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


def home(request):
    return render(request, 'home.html')


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


def addItems(request):
    return render(request, 'addItems.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def userProfile(request):
    return render(request, 'userProfile.html')
