import logging

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from core.models import Exchange
from exchange_rate import settings


class Command(BaseCommand):
    help = 'Request "Diario Oficial de la Federación" service for current ' \
           'exchange rate'

    def handle(self, *args, **options):
        response = requests.get(settings.DIARIO_OFICIAL_URL)
        assert response.status_code == 200, response.text

        soup = BeautifulSoup(response.text, "lxml")

        try:
            exchange_table = soup.find_all('table')[
                settings.DIARIO_OFICIAL_TABLE_POSITION]
            last_row = exchange_table.find_all('tr')[
                settings.DIARIO_OFICIAL_ROW_POSITION]
            for_payments_column = last_row.find_all('td')[
                settings.DIARIO_OFICIAL_COLUMN]
            str_value = for_payments_column.text.strip()

            value = float(str_value)
            Exchange.objects.create(
                value=value,
                provider='diario_oficial'
            )
        except (AttributeError, KeyError, IndexError) as error:
            logging.error(error, exc_info=True)
        except ValueError:
            logging.error('str value error, validate date', exc_info=True)
