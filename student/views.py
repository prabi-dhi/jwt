from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentDetailGetApi(APIView):
    def get(self, request, pk):
        student = Student.objects.get(pk = pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class StudentDetailUpdateApi(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer= StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDetailDeleteApi(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def delete(self, request, pk):
        student = Student.objects.get(pk = pk)
        student.is_deleted = True
        student.save()
        return Response(status= status.HTTP_204_NO_CONTENT)
