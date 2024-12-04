from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('user/', views.UserListApi.as_view()), 
    path('user/add/', views.UserAddApi.as_view()),
    path('user/<int:pk>/', views.UserDetailGetApi.as_view()),
    path('user/update/<int:pk>/', views.UserDetailUpdateApi.as_view()),
    path('user/delete/<int:pk>/', views.UserDetailDeleteApi.as_view()),
] 