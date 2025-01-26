from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class UserTests(APITestCase):
    def setUp(self):
        """ Установка тестовых данных. """

        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

        self.token = RefreshToken.for_user(self.user).access_token
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'role': 'student',
        }

    def test_create_user(self):
        """ Тестирование создания нового пользователя. """

        url = reverse('users:user-list')
        response = self.client.post(url, self.user_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_user_login(self):
        """ Тестирование получения токена через логин. """

        url = reverse('users:token_obtain_pair')
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_role_update(self):
        """ Тестирование обновления роли пользователя. """

        url = reverse('users:user-update-role', kwargs={'pk': self.user.pk})
        role_data = {'role': 'admin'}
        response = self.client.patch(url, role_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.role, 'admin')

    def test_role_update_invalid(self):
        """ Тестирование обновления роли с неверными данными. """

        url = reverse('users:user-update-role', kwargs={'pk': self.user.pk})
        role_data = {'role': 'invalid_role'}
        response = self.client.patch(url, role_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
