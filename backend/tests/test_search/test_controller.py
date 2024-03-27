# writing new unit test cases here
import json

import pytest
from django.test.client import Client

client = Client()


def test_entities_search_api():
    "test method to test the entities search api"
    headers = {"HTTP_X_API_KEY": "xeJJzhaj1mQ-ksTB_nF_iH0z5YdG50yQtwQCzbcHuKA"}
    entities_response = client.get(
        "/api/1/search?q=iit", follow=False, secure=False, **headers
    )
    assert entities_response.status_code == 200


@pytest.mark.django_db
def test_entities_popular_search_api():
    "test method to test the popular search api"
    headers = {"HTTP_X_API_KEY": "xeJJzhaj1mQ-ksTB_nF_iH0z5YdG50yQtwQCzbcHuKA"}
    entities_response = client.get(
        "/api/1/popular-searches", follow=False, secure=False, **headers
    )
    assert entities_response.status_code == 200


@pytest.mark.django_db
def test_entities_search_report_api():
    "test method to test the search report api"
    headers = {"HTTP_X_API_KEY": "xeJJzhaj1mQ-ksTB_nF_iH0z5YdG50yQtwQCzbcHuKA"}
    request_body = {
        "query": "Mains physics",
        "uid": 26330799,
        "start_page": "https://engineering.careers360.com/download/ebooks-and-sample-papers",
        "destination": "www.careers360.com/qna?search=Mains physics",
        "destination_type": "question",
        "device": "Mobile",
        "ip": "157.47.94.225",
        "add_question_status": 1,
    }

    entities_response = client.post(
        "/api/1/search-report",
        json.dumps(request_body),
        content_type="application/json",
        follow=False,
        secure=False,
        **headers
    )
    assert entities_response.status_code == 200
