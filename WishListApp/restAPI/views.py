from django.shortcuts import render
from django.http import HttpResponse

import json

from WishListApp.restAPI.models import Item

# Create your views here.
def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')
