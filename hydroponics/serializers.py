from rest_framework import serializers
from .models import System

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'name', 'location', 'status', 'owner']
        read_only_fields = ['owner']

    def create(self, validated_data):
        # Assign the owner from the request user
        validated_data['owner'] = self.context['request'].user
        return System.objects.create(**validated_data)