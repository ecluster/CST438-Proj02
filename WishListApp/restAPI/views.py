from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
import json

# Create your views here.
class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        query = self.request.GET.get('search')
        if query is not None:
            user = user.filter(name__contains=query) | user.filter(creator__contains=query)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

