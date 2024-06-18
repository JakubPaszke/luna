from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import SensorData
from hydroponics.models import System

User = get_user_model()

class SensorDataTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.system = System.objects.create(name='Test System', owner=self.user)
        self.sensor_data = SensorData.objects.create(system=self.system, ph=6.5, temperature=20.0, tds=400.0)

    def test_create_sensor_data(self):
        url = reverse('sensor-list')
        data = {
            'system': self.system.id,
            'ph': 6.8,
            'temperature': 21.0,
            'tds': 410.0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SensorData.objects.count(), 2)

    def test_list_sensor_data(self):
        other_user = User.objects.create_user(username='otheruser2', password='123456')
        other_system = System.objects.create(name='Other Test System', owner=other_user)
        SensorData.objects.create(system=other_system, ph=7.0, temperature=22.0, tds=450.0)

        url = reverse('sensor-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_count = SensorData.objects.filter(system__owner=self.user).count()
        self.assertEqual(len(response.data['results']), expected_count)


    def test_retrieve_sensor_data(self):
        url = reverse('sensor-detail', kwargs={'pk': self.sensor_data.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ph'], f"{self.sensor_data.ph:.2f}")


    def test_update_sensor_data(self):
        url = reverse('sensor-detail', kwargs={'pk': self.sensor_data.id})
        data = {
            'system': self.system.id,
            'ph': 7.0,
            'temperature': 22.0,
            'tds': 420.0
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sensor_data.refresh_from_db()
        self.assertEqual(self.sensor_data.ph, 7.0)

    def test_delete_sensor_data(self):
        url = reverse('sensor-detail', kwargs={'pk': self.sensor_data.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SensorData.objects.count(), 0)
