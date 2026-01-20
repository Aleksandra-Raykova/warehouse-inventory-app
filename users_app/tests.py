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


class CustomUserManagerTest(TestCase):
    def test_create_superuser_works_correct(self):
        user = CustomUser.objects.create_superuser("test@test.com", "123456789")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.check_password("123456789"))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_user_must_have_email_when_created(self):
        with self.assertRaises(ValueError) as error:
            CustomUser.objects.create_user(email="", password="132456789")

        self.assertEqual(str(error.exception), "Users must have an email address")

    def test_superuser_cannot_be_is_staff_False(self):
        with self.assertRaises(ValueError) as error:
            CustomUser.objects.create_superuser(email="test@test.com", password="123456789", is_staff=False)
        self.assertEqual(str(error.exception), 'Superuser must have is_staff=True.')

    def test_superuser_cannot_be_is_superuser_False(self):
        with self.assertRaises(ValueError) as error:
            CustomUser.objects.create_superuser(email="test@test.com", password="123456789", is_superuser=False)
        self.assertEqual(str(error.exception), 'Superuser must have is_superuser=True.')

