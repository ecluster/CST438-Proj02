from django.forms import ModelForm
from .models import User
from.models import Item
from.models import Wishlist
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['itemId', 'name', 'imageURL', 'websiteURL']

class AddtoWislistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['wishListId', 'userid', 'itemId']
class UserAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


