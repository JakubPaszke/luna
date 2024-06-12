from django.test import TestCase
from django.contrib.auth.models import User
from .models import SensorData
from hydroponics.models import System
from django.utils import timezone

class SensorDataTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.system = System.objects.create(owner=self.user, name="Test System")

    def test_create_sensor_data(self):
        sensor_data = SensorData.objects.create(
            system=self.system,
            ph=7.0,
            temperature=20.0,
            tds=500,
            created_time=timezone.now()
        )
        self.assertEqual(sensor_data.ph, 7.0)
        self.assertEqual(sensor_data.system, self.system)

    def test_update_sensor_data(self):
        sensor_data = SensorData.objects.create(
            system=self.system,
            ph=7.0,
            temperature=20.0,
            tds=500,
            created_time=timezone.now()
        )
        sensor_data.ph = 8.0
        sensor_data.save()

        updated_data = SensorData.objects.get(id=sensor_data.id)
        self.assertEqual(updated_data.ph, 8.0)

    def test_soft_delete_sensor_data(self):
        sensor_data = SensorData.objects.create(
            system=self.system,
            ph=7.0,
            temperature=20.0,
            tds=500,
            created_time=timezone.now()
        )
        sensor_data.delete()

        self.assertTrue(SensorData.all_objects.filter(id=sensor_data.id).exists())
        self.assertTrue(sensor_data.is_deleted)