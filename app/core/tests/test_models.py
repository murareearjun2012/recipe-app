from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_success(self):
        email = 'test@gmail.com'
        password = 'test@124'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalised(self):
        email = 'test@WELLA.COM'
        user = get_user_model().objects.create_user(email, email)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
         'test@gmail.com', 'test@123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
