from django.test import TestCase
from django.contrib.auth.models import User
from .models import System

class SystemTests(TestCase):
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