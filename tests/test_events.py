import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient

from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_get_events_returns_all_events_and_status_code_200(client):
    response = client.get("/events")
    assert response.status_code == 200
    assert len(response.json()["events"]) == 5

def test_get_events_return_includes_location_name(client):
    response = client.get("/events")
    assert response.status_code == 200
    locations = [event["location"] for event in response.json()["events"]]
    assert "venue_b" in locations

def test_get_events_returns_events_in_asc_order_of_start_datetime_and_location(client):
    response = client.get("/events")
    event_order = [event["id"] for event in response.json()["events"]]
    assert event_order == [3, 4, 1, 5, 2]