from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Creating new user with an email is successful."""
        email = "admin@example.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Normalize user email when creating new user."""
        email = "admin@EXAMPLE.cOM"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_invalid_user_email_raises_error(self):
        """Raise error when creating user with invalid email."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password="password"
            )

    def test_create_super_user(self):
        """Create super user is successful"""
        user = get_user_model().objects.create_superuser(
            "admin@example.com",
            "password"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

