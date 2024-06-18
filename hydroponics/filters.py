import django_filters
from .models import System

class SystemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    created_time_min = django_filters.DateTimeFilter(field_name='created_time', lookup_expr='gt')
    created_time_max = django_filters.DateTimeFilter(field_name='created_time', lookup_expr='lt')

    class Meta:
        model = System
        fields = ['name', 'location', 'status', 'created_time']
