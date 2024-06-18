from django.test import TestCase
from .models import System
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

User = get_user_model()

# Model Tests
class SystemModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_system(self):
        system = System.objects.create(
            owner=self.user,
            name="Test System",
            location="Test Location",
            status="active"
        )
        self.assertEqual(system.name, "Test System")
        self.assertEqual(system.owner, self.user)

    def test_update_system(self):
        system = System.objects.create(
            owner=self.user,
            name="Initial Name",
            location="Test Location",
            status="active"
        )
        system.name = "Updated Name"
        system.save()

        updated_system = System.objects.get(id=system.id)
        self.assertEqual(updated_system.name, "Updated Name")

    def test_soft_delete_system(self):
        system = System.objects.create(
            owner=self.user,
            name="Test System",
            location="Test Location",
            status="active"
        )
        system.delete()

        self.assertTrue(System.all_objects.filter(id=system.id).exists())
        self.assertTrue(system.is_deleted)

# API Tests
class SystemAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.system = System.objects.create(owner=self.user, name='Test System')

    def test_create_system(self):
        url = reverse('system-list')
        data = {'name': 'New System'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(System.objects.count(), 2)
        self.assertEqual(System.objects.get(id=2).name, 'New System')

    def test_list_systems(self):
        System.objects.create(owner=self.user, name='Test System 2')
        System.objects.create(owner=self.user, name='Test System 3')
        System.objects.create(owner=User.objects.create_user(username='otheruser', password='12345'), name='Other System')

        url = reverse('system-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_systems = System.objects.filter(owner=self.user).count()
        self.assertEqual(len(response.data['results']), user_systems) 

    def test_retrieve_system(self):
        url = reverse('system-detail', kwargs={'pk': self.system.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.system.name)

    def test_update_system(self):
        url = reverse('system-detail', kwargs={'pk': self.system.id})
        data = {'name': 'Updated System'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.system.refresh_from_db()
        self.assertEqual(self.system.name, 'Updated System')

    def test_delete_system(self):
        url = reverse('system-detail', kwargs={'pk': self.system.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(System.objects.count(), 0)
