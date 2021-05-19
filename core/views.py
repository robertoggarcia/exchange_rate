from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Exchange
from core.serializers import ExchangeSerializer


@api_view(['GET'])
def get_exchange_rate(request):
    provider = ['fixer', 'diario_oficial', 'banxico']
    data = {"rates": []}
    for provider in provider:
        exchange_rate = Exchange.objects.filter(
            provider=provider
        ).order_by('-last_updated').first()

        data['rates'].append(ExchangeSerializer(exchange_rate).data)

    return Response(data=data, status=status.HTTP_200_OK)
