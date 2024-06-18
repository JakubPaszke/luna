from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework.permissions import IsAuthenticated

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class SensorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]