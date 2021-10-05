# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import UserSerializer
# from .models import User
# import json
from django.shortcuts import render

# Create your views here.
# class UserList(APIView):
#     def get(self, request):
#         print("**************\n", request.method)
#         if request.method == "GET":
#             user = User.objects.all()
#             query = self.request.GET.get('search')
#             if query is not None:
#                 user = user.filter(name__contains=query) | user.filter(creator__contains=query)
#             serializer = UserSerializer(user, many=True)
#             json_obj = json.dumps(serializer.data)
#             print(json_obj)
#             return Response(serializer.data)


def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')