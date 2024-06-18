from rest_framework import generics
from .models import System
from .serializers import SystemSerializer
from rest_framework.permissions import IsAuthenticated

class SystemListCreateAPIView(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SystemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = [IsAuthenticated]