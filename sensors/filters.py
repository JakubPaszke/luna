import django_filters
from .models import SensorData

class SensorDataFilter(django_filters.FilterSet):
    ph_min = django_filters.NumberFilter(field_name='ph', lookup_expr='gt')
    ph_max = django_filters.NumberFilter(field_name='ph', lookup_expr='lt')
    temperature_min = django_filters.NumberFilter(field_name='temperature', lookup_expr='gt')
    temperature_max = django_filters.NumberFilter(field_name='temperature', lookup_expr='lt')
    tds_min = django_filters.NumberFilter(field_name='tds', lookup_expr='gt')
    tds_max = django_filters.NumberFilter(field_name='tds', lookup_expr='lt')
    created_time_min = django_filters.DateTimeFilter(field_name='created_time', lookup_expr='gt')
    created_time_max = django_filters.DateTimeFilter(field_name='created_time', lookup_expr='lt')

    class Meta:
        model = SensorData
        fields = ['ph', 'temperature', 'tds', 'created_time']
