# writing new unit test cases here
import json

import pytest
from django.test.client import Client

client = Client()

@pytest.mark.django_db
def test_weather_history_api():
    "test method to test the weather history api"
    headers = {"HTTP_X_API_KEY": "xeJJzhaj1mQ-ksTB_nF_iH0z5YdG50yQtwQCzbcHuKA"}
    entities_response = client.get(
        "/api/1/weather-history?from_date=24-03-202&to_date=27-03-2024", follow=False, secure=False, **headers
    )
    assert entities_response.status_code == 200