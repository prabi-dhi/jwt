from rest_framework import serializers
from .models import User
from student.models import Student
from teacher.models import Teacher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','user_type']
    
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        user_type = validated_data.get('user_type')
        user = User.objects.create(username=username, password=password, email = email, user_type = user_type)
        if user.user_type == 'STUDENT':
            Student.objects.create(user=user, student_name = username)
        elif user.user_type == 'TEACHER':
            Teacher.objects.create(user = user, teacher_name = username)
        return user


