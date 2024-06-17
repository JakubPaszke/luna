from django.db import models
from hydroponics.models import System
from luna.common.managers import ActiveObjects

class SensorData(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    tds = models.DecimalField(max_digits=5, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
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
        return f"{self.system.name} at {self.created_time}"
