from django.test import TestCase

from users_app.models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.u = CustomUser.objects.create_user("test@test.com", "123456789")

    def test_all_fields_in_db(self):
        fields = [f.name for f in CustomUser._meta.fields]
        self.assertIn("email", fields)
        self.assertIn("first_name", fields)
        self.assertIn("last_name", fields)
        self.assertIn("is_active", fields)
        self.assertIn("is_staff", fields)
        self.assertIn("is_superuser", fields)
        self.assertIn("id", fields)
        self.assertIn("password", fields)
        self.assertIn("date_joined", fields)
        self.assertIn("last_login", fields)

    def test_create_user_all_correct(self):
        self.assertEqual(self.u.email, 'test@test.com')
        self.assertEqual(self.u.first_name, '')
        self.assertEqual(self.u.last_name, '')
        self.assertTrue(self.u.is_active)
        self.assertFalse(self.u.is_staff)
        self.assertFalse(self.u.is_superuser)
