import random

import factory


class ExchangeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'core.Exchange'

    value = 20.0
    provider = random.choice(['fixer', 'diario_oficial', 'banxico'])
