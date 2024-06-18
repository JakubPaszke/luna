from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', SensorListCreateAPIView.as_view(), name='sensor-list'),
    path('<int:pk>/', SensorRetrieveUpdateDestroyAPIView.as_view(), name='sensor-detail'),
]
