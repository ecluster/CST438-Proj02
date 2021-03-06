from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .serializer import ItemSerializer
from .serializer import WishListSerializer
from .models import User
from .models import Item
from .models import Wishlist
from django.contrib.auth import authenticate, login, logout
import json
from .forms import UserForm
from .forms import CreateItemForm
from .forms import AddtoWislistForm
from .forms import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from rest_framework.decorators import api_view

from django.shortcuts import render, redirect
from django.urls import path
from . import views

import requests

# --------------------- Item API --------------------------
# show all items in data base
@api_view(['GET'])
def items_list_api(request):
    # List all code snippets
    if request.method == 'GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        print("******")
        return Response(serializer.data)

# Show specific item / delete specific item --> by itemId
@api_view(['GET', 'DELETE', 'PATCH'])
def item_detail(request, iId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=iId)
        serializer = ItemSerializer(item, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        item = Item.objects.get(itemId=iId)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item = Item.objects.get(itemId=iId)
        item.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Delete an Item
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def deleteItem(request, iId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=iId)
        serializer = ItemSerializer(item, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return render(request, 'AdminItemDelete.html', {"item": item})
    if request.method == 'POST':
        item = Item.objects.get(itemId=iId)
        item.delete()
        return render(request, 'AdminHome.html')


# Create an Item
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update an Item
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def update_item(request, iId, iName, iImgURl, iWebURL):
    item = Item.objects.get(itemId=iId)
    item.itemId = iId
    item.name = iName
    item.imageURL = iImgURl
    item.websiteURL = iWebURL
    item.save()
    return Response(status=status.HTTP_202_ACCEPTED)
# Update a Item
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def updateItem(request, iId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=iId)
        serializer = ItemSerializer(item, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return render(request, 'AdminItemUpdate.html', {'item': item})
    elif request.method == 'POST':
        print("Post: ", json.loads(json.dumps(request.POST)))
        obj = json.loads(json.dumps(request.POST))
        obj_id = obj["itemId"]
        obj_name = obj["name"]
        obj_img = obj["imageURL"]
        obj_web = obj["websiteURL"]
        url = 'http://127.0.0.1:8000/item-change/{}/{}/{}/{}/'.format(obj_id, obj_name, obj_img, obj_web)
        requests.post(url)
        return render(request, 'AdminHome.html')


# --------------------- Wishlist API --------------------------
# Update wishlist
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def update_wish(request, wId, uId, iId):
    wish = Wishlist.objects.get(wishListId=wId)
    wish.wishListId = wId
    wish.userid = uId
    wish.itemId = iId
    wish.save()
    return Response(status=status.HTTP_202_ACCEPTED)
# Update a Item
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def updateWish(request, wId):
    if request.method == 'GET':
        wish = Wishlist.objects.get(wishListId=wId)
        serializer = WishListSerializer(wish, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return render(request, 'AdminWishUpdate.html', {'wish': wish})
    elif request.method == 'POST':
        print("Post: ", json.loads(json.dumps(request.POST)))
        obj = json.loads(json.dumps(request.POST))
        obj_id = obj["wishListId"]
        obj_uId = obj["userid"]
        obj_iId = obj["itemId"]
        url = 'http://127.0.0.1:8000/wish-change/{}/{}/{}/'.format(obj_id, obj_uId, obj_iId)
        requests.post(url)
        return render(request, 'AdminHome.html')

# show all wishlists in data base
@api_view(['GET'])
def wish_list_api(request):
    # List all code snippets
    if request.method == 'GET':
        wish = Wishlist.objects.all()
        serializer = WishListSerializer(wish, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        print("******")
        return Response(serializer.data)

# Create a wishlist
@api_view(['POST'])
def create_wishlist(request):
    serializer = WishListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(json.loads(json.dumps(serializer.data)))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Show multiple wishlist --> by user ID
@api_view(['GET'])
def wishlist_user(request, uId):
    if request.method == 'GET':
        wList = Wishlist.objects.filter(userid=uId)
        serializer1 = WishListSerializer(wList, many=True)
        json1 = json.loads(json.dumps(serializer1.data))
        print(json1)
        return Response(serializer1.data)


# Show specific items of a wishlist from a user --> by wishListId
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


# Show all items saved --> by user ID
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

# Delete a user
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def deleteWish(request, wId):
    if request.method == 'GET':
        wish = Wishlist.objects.get(wishListId=wId)
        serializer = WishListSerializer(wish, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return render(request, 'AdminWishDelete.html', {"wish": wish})
    if request.method == 'POST':
        wish = Wishlist.objects.get(wishListId=wId)
        wish.delete()
        return render(request, 'AdminHome.html')


# --------------------- User API --------------------------
# Show all users
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


# Show user detail / delete user / update user --> by username
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def user_detail(request, uName):
    # List all code snippets
    if request.method == 'GET':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)


# Delete a user
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def deleteUser(request, uName):
    if request.method == 'GET':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, many=False)
        json_obj = json.loads(json.dumps(serializer.data))
        print(json_obj)
        return render(request, 'AdminDelete.html', {"user": user})
    if request.method == 'POST':
        user = User.objects.get(username=uName)
        user.delete()
        return render(request, 'AdminHome.html')


@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def update_user(request, uId, uName, uPassword):
    user = User.objects.get(username=uName)
    user.userId = uId
    user.username = uName
    user.password = uPassword
    user.save()
    return Response(status=status.HTTP_202_ACCEPTED)


# Update a user
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def updateUser(request, uName):
    if request.method == 'GET':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return render(request, 'AdminUpdate.html', {'user': user})
    elif request.method == 'POST':
        print("Post: ", json.loads(json.dumps(request.POST)))
        obj = json.loads(json.dumps(request.POST))
        obj_id = obj["userId"]
        obj_username = obj["username"]
        obj_password = obj["password"]
        url = 'http://127.0.0.1:8000/user-change/{}/{}/{}/'.format(obj_id, obj_username, obj_password)
        requests.post(url)
        return render(request, 'AdminHome.html')


@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def updateUserProfile(request, uName):
    if request.method == 'GET':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return render(request, 'userProfile.html', {'user' : user})
    elif request.method == 'POST':
        user = User.objects.get(username=uName)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'home.html')
        return render(request, 'home.html')


# create a user
# @api_view(['POST'])
def createAccount(request):
    form = UserCreationForm()
    if request.method == 'POST':
        # print('Printing POST: ' , request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #<- saves in the database
            print(form.data)
            User.objects.create(userId = form.data['userId'] ,
                                username=form.data['username'],
                                password= form.data['password1'])
            return redirect('/login/')

    context = {'form': form}
    return render(request, 'createAccount.html', context)


def home(request):
    url = 'http://127.0.0.1:8000/all-user-items/1/'
    obj = requests.get(url).json()
    return render(request, 'home.html', {'allItems' : obj})

def addItems(request):
    form = CreateItemForm()
    if request.method == 'POST':
        # print('Printing POST: ' , request.POST)
        form = CreateItemForm(request.POST)
        print(json.loads(json.dumps(form.data)))
        if form.is_valid():
            form.save()  # <- saves in the database
            return redirect('../home/')

    context = {'form': form}
    return render(request, 'addItems.html', context)


def addToWishlist(request):
    form = AddtoWislistForm()
    if request.method == 'POST':
        # print('Printing POST: ' , request.POST)
        form = AddtoWislistForm(request.POST)
        print(json.loads(json.dumps(form.data)))
        if form.is_valid():
            form.save()  # <- saves in the database
            return redirect('../home/')

    context = {'form': form}
    return render(request, 'addToWishlist.html', context)


def adminHome(request):
    return render(request, 'AdminHome.html')


def adminUsers(request):
    url = 'http://127.0.0.1:8000/users/'
    obj = requests.get(url).json()
    return render(request, 'AdminUsers.html', {"allUsers": obj})


def adminItems(request):
    url = 'http://127.0.0.1:8000/item-list-API/'
    obj = requests.get(url).json()
    return render(request, 'AdminItems.html', {"allItems": obj})

def adminWishlist(request):
    url = 'http://127.0.0.1:8000/wish-list-api/'
    obj = requests.get(url).json()
    return render(request, 'AdminWishlist.html', {"allWish": obj})


def adminDelete(request):
    return render(request, 'AdminDelete.hmtl')

def adminDeleteItems(request):
    return render(request, 'AdminItemDelete.html')

def adminDeleteWish(request):
    return render(request, 'AdminWishDelete.html')


def adminUpdate(request):
    return render(request, 'AdminUpdate.hmtl')

def adminUpdateItems(request):
    return render(request, 'AdminItemUpdate.html')

def adminUpdateWish(request):
    return render(request, 'AdminWishUpdate.html')


def wishlist(request):
    return render(request, 'wishlist.html')

def userProfile(request):
    return render(request, 'userProfile.html')

def welcome(request):
    return render(request, 'welcome.html')

def loginPage(request):
    print("got to page")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("here")
        if user is not None:
            print("should redirect")
            if user.is_staff:
                print("staff redirect")
                login(request, user)
                return redirect('/AdminHome/')
            else:
                login(request, user)
                return redirect('/home/')
        else:
            print("did not redirect")
            return render(request, 'login.html')
    context = {}
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def createAdmin(request):
    form = UserCreationForm()
    if request.method == 'POST':
        # form = UserForm(request.POST)
        # print(request.POST.get('username'))
        # login(request, user)
        # print('Printing POST: ' , request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # <- saves in the database
            User.objects.create(userId=form.data['userId'],
                                username=form.data['username'],
                                password=form.data['password1'])

            userAdmin = authenticate(request, username=form.data['username'], password=form.data['password1'])
            userAdmin.is_staff = True
            userAdmin.save()
            print(userAdmin.is_staff)
            return redirect('/AdminHome/')

    context = {'form': form}
    return render(request, 'createAdminAccount.html', context)

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("should redirect")
            login(request, user)
            return redirect('/AdminHome/')
        else:
            print("did not redirect")
            return render(request, 'adminLogin.html')
    context = {}
    return render(request, 'adminLogin.html')

def showSpecificItems(request):
    url = 'http://127.0.0.1:8000/specific-wishlitst-items/1/'
    obj = requests.get(url).json()
    return render(request, 'UserChoiceWish.html', {'allItems' : obj})
