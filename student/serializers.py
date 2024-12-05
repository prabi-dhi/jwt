from rest_framework import serializers
from user.models import User
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True) 
    password = serializers.CharField(write_only=True) 
    email = serializers.CharField(write_only = True)
    user_name = serializers.ReadOnlyField(source='user.username') 
    user_email = serializers.ReadOnlyField(source = 'user.email')
    # users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many = True, required = False) 

    class Meta:
        model = Student
        fields = ['id', 'student_name', 'username', 'password', 'email','user_name','user_email']

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        student_name = validated_data.get('student_name')
        
        user = User.objects.create(username=username, password=password, email = email)
        student = Student.objects.create(student_name=student_name, user =user)
        return student