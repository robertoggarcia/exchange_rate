from rest_framework import serializers

from core.models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('value', 'provider', 'last_updated')
