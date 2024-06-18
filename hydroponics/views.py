from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import System
from .serializers import SystemSerializer, SystemDetailSerializer
from .filters import SystemFilter
from rest_framework.permissions import IsAuthenticated

class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SystemListCreateAPIView(generics.ListCreateAPIView):
    queryset = System.objects.all().order_by('id')
    serializer_class = SystemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SystemFilter
    ordering_fields = ['name', 'location', 'status', 'created_time']
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        return System.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SystemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return System.objects.filter(owner=self.request.user)