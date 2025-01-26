from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from modules.models import EducationModule, Lesson
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class EducationModuleTests(APITestCase):
    def setUp(self):
        """ Установка тестовых данных. """

        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.headers = {'Authorization': f'Bearer {self.token}'}

        self.module_data = {
            'order': 1,
            'title': 'Test Module',
            'description': 'This is a test module.',
        }
        self.module = EducationModule.objects.create(**self.module_data)

    def test_create_education_module(self):
        """ Тестирование создания образовательного модуля. """

        url = reverse('modules:module-list')
        response = self.client.post(url, self.module_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Module')

    def test_list_education_modules(self):
        """ Тестирование получения списка образовательных модулей. """

        url = reverse('modules:module-list')
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_publish_education_module(self):
        """ Тестирование публикации образовательного модуля. """

        url = reverse('modules:module-publish', kwargs={'pk': self.module.pk})
        response = self.client.post(url, {}, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module.refresh_from_db()
        self.assertTrue(self.module.is_published)

    def test_create_lesson_in_module(self):
        """ Тестирование создания урока в образовательном модуле. """

        lesson_data = {
            'module': self.module.pk,
            'title': 'Test Lesson',
            'description': 'This is a test lesson.',
            'order': 1
        }
        url = reverse('modules:lesson-list')
        response = self.client.post(url, lesson_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Lesson')


class LessonTests(APITestCase):
    def setUp(self):
        """ Установка тестовых данных. """

        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.headers = {'Authorization': f'Bearer {self.token}'}

        self.module = EducationModule.objects.create(
            order=1,
            title='Test Module',
            description='This is a test module.'
        )
        self.lesson_data = {
            'module': self.module.pk,
            'title': 'Test Lesson',
            'description': 'This is a test lesson.',
            'order': 1
        }

    def test_create_lesson(self):
        """ Тестирование создания урока. """

        url = reverse('modules:lesson-list')
        response = self.client.post(url, self.lesson_data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Lesson')

    def test_list_lessons(self):
        """ Тестирование получения списка уроков. """
        url = reverse('modules:lesson-list')
        self.client.post(reverse('modules:lesson-list'), self.lesson_data, format='json', **self.headers)
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
