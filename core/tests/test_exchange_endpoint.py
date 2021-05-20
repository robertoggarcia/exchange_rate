from django.contrib.auth.models import User
from django.test import TestCase

from core.tests.factories import ExchangeFactory


class TestExchangeEndpoint(TestCase):

    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:8000/'
        User.objects.create_user(
            username='user',
            password='password'
        )
        response = self.client.post(f'{self.host}api/token/', {
            'username': 'user',
            'password': 'password'
        })
        self.token = response.json()['access']

    def test_get_exchange_rates(self):
        providers = ['fixer', 'diario_oficial', 'banxico']
        for provider in providers:
            ExchangeFactory(provider=provider)

        response = self.client.get(f'{self.host}v1/exchange_rate/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')

        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['rates']), 3)
