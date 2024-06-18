from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'system', 'ph', 'temperature', 'tds', 'created_time']
        read_only_fields = ['created_time']

    def validate_system(self, value):
        if value.owner != self.context['request'].user:
            raise serializers.ValidationError("You do not own this system.")
        return value