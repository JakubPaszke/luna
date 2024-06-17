from django.db import models
from django.contrib.auth.models import User
from luna.common.managers import ActiveObjects

class System(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, default='active')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveObjects() 
    all_objects = models.Manager()  

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def __str__(self):
        return self.name
