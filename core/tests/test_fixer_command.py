from django.test import TestCase
from unittest import mock
from unittest.mock import Mock

from core.management.commands.fixer_provider import Command
from core.models import Exchange


@mock.patch('core.management.commands.fixer_provider.requests')
class TestFixerCommand(TestCase):
    def mock_get(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'rates': {'MXN': 19.00}}
        return response_mock

    def test_fixer_command_execution(self, response_mock):
        response_mock.get.side_effect = self.mock_get

        command = Command()
        command.handle()

        self.assertTrue(response_mock.get.called)
        self.assertEqual(Exchange.objects.filter(provider='fixer').count(), 1)
