from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class TeacherListApi(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer= TeacherSerializer(teacher, many= True)
        return Response(serializer.data)
    
class TeacherAddApi(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

