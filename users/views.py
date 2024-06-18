from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


