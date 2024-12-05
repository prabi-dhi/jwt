from rest_framework import serializers
from .models import Teacher
from user.models import User

class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True) 
    password = serializers.CharField(write_only=True) 
    email = serializers.CharField(write_only = True)
    user_name = serializers.ReadOnlyField(source='user.username') 
    user_email = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name','username', 'password', 'email','user_name','user_email']

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        teacher_name = validated_data.get('teacher_name')

        user = User.objects.create(username=username, password=password, email = email, user_type = 'TEACHER')
        teacher = Teacher.objects.create(teacher_name = teacher_name, user = user)
        return teacher

        
