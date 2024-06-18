from django.urls import path
from .views import UserRegistrationAPIView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]