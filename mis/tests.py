from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from django.urls import reverse


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user_1 = User.objects.create(username='test_username', password='test_password')

    def setUp(self):
        self.client = APIClient()

    def test_login_success(self):
        data = {'username': 'test_username', 'password': 'test_password'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_fail(self):
        data = {'username': 'test_username', 'password': 'wrong_password'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_non_existing_user(self):
        data = {'username': 'random_username', 'password': 'random_password'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
