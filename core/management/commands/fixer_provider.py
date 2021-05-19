import logging

import requests
from django.core.management.base import BaseCommand

from core.models import Exchange
from exchange_rate import settings


class Command(BaseCommand):
    help = 'Request Fixer service for current exchange rate'

    def handle(self, *args, **options):
        url = f'{settings.FIXER_URL}latest?' \
              f'access_key={settings.FIXER_API_KEY}&' \
              f'base={settings.FIXER_BASE}&symbols=MXN'
        response = requests.get(url)

        assert response.status_code == 200, response.text

        data = response.json()
        try:
            Exchange.objects.create(
                value=data['rates']['MXN'],
                provider='fixer'
            )
        except (AttributeError, KeyError) as error:
            logging.error(error, exc_info=True)
