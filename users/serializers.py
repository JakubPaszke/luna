from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'additional_info')

    def create(self, validated_data):
        additional_info = validated_data.pop('additional_info', None) 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        if additional_info is not None:
            user.additional_info = additional_info
        user.save()
        return user