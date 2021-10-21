from django.forms import ModelForm
from .models import User
from.models import Item
from.models import Wishlist
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['userId', 'username', 'password']

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['itemId', 'name', 'imageURL', 'websiteURL']

class AddtoWislistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['wishListId', 'userid', 'itemId']

