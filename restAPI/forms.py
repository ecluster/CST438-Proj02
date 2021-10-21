from django.forms import ModelForm
from .models import User
from.models import Item
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['userId', 'username', 'password']

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['itemId', 'name', 'imageURL', 'websiteURL']