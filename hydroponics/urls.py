from django.urls import path
from .views import SystemListCreateAPIView, SystemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', SystemListCreateAPIView.as_view(), name='system-list'),
    path('<int:pk>/', SystemRetrieveUpdateDestroyAPIView.as_view(), name='system-detail'),
]
