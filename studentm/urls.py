from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')), # login and logout views for browsable API
    path('', include('user.urls')),
    path('', include('student.urls')),
    path('', include('classroom.urls')),
    path('', include('teacher.urls')),
    path('',include('subject.urls')),
]