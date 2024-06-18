from rest_framework import serializers
from .models import System
from sensors.models import SensorData
from sensors.serializers import SensorDataSerializer

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'name', 'location', 'status', 'owner', 'created_time']
        read_only_fields = ['owner', 'created_time']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return System.objects.create(**validated_data)
    
    def get_queryset(self):
        return System.objects.filter(owner=self.request.user)
    

class SystemDetailSerializer(serializers.ModelSerializer):
    latest_measurements = serializers.SerializerMethodField()

    class Meta:
        model = System
        fields = ['id', 'name', 'location', 'status', 'owner', 'created_time', 'latest_measurements']
        read_only_fields = ['owner', 'created_time']

    def get_latest_measurements(self, obj):
        latest_measurements = SensorData.objects.filter(system=obj).order_by('-created_time')[:10]
        return SensorDataSerializer(latest_measurements, many=True).data