from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from django.urls import reverse


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='test_username', password='test_password')

    def setUp(self):
        self.client = APIClient()

    def test_login_success(self):
        response = self.client.post('/login/', {'username': 'test_username', 'password': 'test_password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_credentials(self):
        response = self.client.post('/login/', {'username': 'test_username', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_user_not_found(self):
        response = self.client.post('/login/', {'username': 'wrong_username', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
