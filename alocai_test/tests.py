import json

import pytest
from django.test import TestCase, Client, override_settings, modify_settings

api_base = '/api/v1/'


class StatusEndpointTestCase(TestCase):

    def test_healthy(self):
        test_url = api_base + 'status'
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


def test_unhealthy(client):
    test_url = api_base + 'status'
    test_expected_result = {"database": "unhealthy"}

    # verifying success response for get request method
    health_response = client.get(test_url)

    assert health_response.status_code == 503
    assert health_response.json() == test_expected_result

    # verifying success response for head request method
    health_response = client.head(test_url)
    assert health_response.status_code == 503
    assert health_response.content == b''
