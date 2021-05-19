from django.urls import path

from core.views import get_exchange_rate

urlpatterns = [
    path('exchange_rate/', get_exchange_rate),
]
