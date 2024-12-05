from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(write_only=True) 
    # password = serializers.CharField(write_only=True) 
    # email = serializers.CharField(write_only = True)
    # user_name = serializers.ReadOnlyField(source='user.username') 
    # email = serializers.ReadOnlyField(source = 'user.email')
    # user= serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name','user','username', 'password', 'email','user_name','email']

    # def create(self, validated_data):
        
