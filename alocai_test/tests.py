import json

from django.test import TestCase, Client, override_settings, modify_settings
from django.conf import settings

from games.models import Game


class StatusEndpointTestCase(TestCase):
    api_base = '/api/v1/'

    def test_healthy(self):
        test_url = self.api_base + 'status'
        test_expected_result = {"database": "healthy"}

        test_client = Client()
        # verifying success response for get request method
        health_response = test_client.get(test_url)

        self.assertEqual(health_response.status_code, 200)
        self.assertEqual(health_response.json(), test_expected_result)

        # verifying success response for head request method
        health_response = test_client.head(test_url)
        self.assertEqual(health_response.status_code, 200)
        self.assertEqual(health_response.content, b'')
