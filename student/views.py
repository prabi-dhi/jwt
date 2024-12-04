from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsUserOrReadOnly

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticated]
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
class StudentListGetApi(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many= True)
        return Response(serializer.data)

class StudentAddApi(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_by = self.request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailGetApi(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({"detail":"Student not found"}, status= status.HTTP_404_NOT_FOUND)

class StudentDetailUpdateApi(APIView):
    permission_classes=[IsAuthenticated, IsUserOrReadOnly]
    def put(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        serializer= StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDetailDeleteApi(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.is_deleted = True
        student.save()
        return Response(status= status.HTTP_204_NO_CONTENT)
