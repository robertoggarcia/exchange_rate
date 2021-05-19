import logging
from datetime import datetime

import requests
from django.core.management.base import BaseCommand

from core.models import Exchange
from exchange_rate import settings


class Command(BaseCommand):
    help = 'Request Banxico service for current exchange rate'

    def handle(self, *args, **options):
        url = f'{settings.BANXICO_URL}' \
              f'{settings.BANXICO_SERIE}/datos/oportuno?' \
              f'token={settings.BANXICO_TOKEN}'
        response = requests.get(url)

        assert response.status_code == 200, response.text

        data = response.json()
        try:
            value = data['bmx']['series'][0]['datos'][0]['dato']
            Exchange.objects.create(
                value=value,
                provider='banxico'
            )
        except (AttributeError, KeyError, IndexError) as error:
            logging.error(error, exc_info=True)
