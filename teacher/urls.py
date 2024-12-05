from django.urls import path, include
from teacher import views

urlpatterns = [
    path('teacher/', views.TeacherListApi.as_view()),
    path('teacher/add/', views.TeacherAddApi.as_view()),
]