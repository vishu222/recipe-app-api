from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_creating_user_with_email_successful(self):
        """create a user with email and password"""
        email = 'test@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalised(self):
        """make the email address normalised"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEqual(user.email, email.lower())

    def test_user_with_invalid_email_address(self):
        """Test creating a user with invalid email address and raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_user_to_be_superuser(self):
        """run a test to find whether the user is a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'Test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
