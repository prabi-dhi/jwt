from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Student
        fields = ['id','name','user']