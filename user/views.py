from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
from .models import User
from .serializers import UserSerializer
from rest_framework import status
  
class UserListApi(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserAddApi(APIView):
    def post(self, request):
        serializer= UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class UserDetailGetApi(APIView):
    def get(Self, request, pk):
        user= User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserDetailUpdateApi(APIView):
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailDeleteApi(APIView):
    def delete(self, request, pk):
        user = User.objects.get(pk = pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)