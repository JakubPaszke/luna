from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    additional_info = models.TextField(null=True, blank=True)