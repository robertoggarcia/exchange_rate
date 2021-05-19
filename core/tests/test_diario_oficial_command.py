from django.test import TestCase
from unittest import mock
from unittest.mock import Mock

from core.management.commands.diario_oficial_provider import Command
from core.models import Exchange


@mock.patch('core.management.commands.diario_oficial_provider.requests')
class TestDiarioOficialCommand(TestCase):
    def mock_get(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.text = open(
            'core/tests/diario_oficial_response.txt').read()
        return response_mock

    def test_diario_oficial_command_execution(self, response_mock):
        response_mock.get.side_effect = self.mock_get

        command = Command()
        command.handle()

        self.assertTrue(response_mock.get.called)
        self.assertEqual(Exchange.objects.filter(
            provider='diario_oficial').count(), 1)
