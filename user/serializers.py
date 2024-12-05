from rest_framework import serializers
from .models import User
from student.models import Student

class UserSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),many = True, view_name= 'student-detail', required = False)
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),many = True, required = False)
    # student = serializers.ReadOnlyField(source='student.student_name') 

    class Meta:
        model = User
        fields = ['id', 'username','email', 'students']