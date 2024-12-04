from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Student
        fields = ['id','student_name','created_by']