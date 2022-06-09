import random

from django.urls import include, path
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase, URLPatternsTestCase


class APITests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    client: APIClient
    equation_endpoint = reverse('api:guess')

    def setUp(self):
        self.client = APIClient()

    def test_answer(self):
        """Тестирование валидного ответа."""

        data = {'number': random.randint(1, 100)}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(response.data['color_name'], ['green', 'blue', 'red'])

    def test_error_if_no_parameters_passed(self):
        """Тестирование ответа, если не переданы параметры."""

        response = self.client.post(
            self.equation_endpoint, data={}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['number'][0]), 'Обязательное поле.')

    def test_error_if_number_less_than_1(self):
        """Тестирование ответа, если number < 1."""

        data = {'number': -1}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['number'][0],
            'Убедитесь, что это значение больше либо равно 1.')

    def test_error_if_number_more_than_100(self):
        """Тестирование ответа, если number > 100."""

        data = {'number': 404}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['number'][0],
            'Убедитесь, что это значение меньше либо равно 100.')
