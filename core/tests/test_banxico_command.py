from django.test import TestCase
from unittest import mock
from unittest.mock import Mock

from core.management.commands.banxico_provider import Command
from core.models import Exchange


@mock.patch('core.management.commands.banxico_provider.requests')
class TestBanxicoCommand(TestCase):
    def mock_get(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'bmx': {'series': [
            {'datos': [{'dato': 19.0}]}
        ]}}
        return response_mock

    def test_banxico_command_execution(self, response_mock):
        response_mock.get.side_effect = self.mock_get

        command = Command()
        command.handle()

        self.assertTrue(response_mock.get.called)
        self.assertEqual(Exchange.objects.filter(provider='banxico').count(), 1)
