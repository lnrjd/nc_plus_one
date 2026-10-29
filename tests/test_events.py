import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


""" Test /events endpoint """

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


""" Test /events/{event_id} endpoint"""

def test_get_event_returns_status_code_200(client):
    response = client.get("/events/1")
    assert response.status_code == 200
    
def test_get_event_response_body_is_single_object_with_event_key(client):
    response = client.get("/events/1")
    assert isinstance(response.json()["event"], dict)

def test_get_event_returns_single_event_with_correct_id(client):
    response = client.get("/events/2")
    assert response.json()["event"]["id"] == 2

def test_get_event_response_includes_venue_details(client):
    response = client.get("/events/1")
    assert response.json()["event"]["location"] == "venue_a"
    assert response.json()["event"]["address"] == "address_a"
    assert response.json()["event"]["capacity"] == 10


def test_get_event_returns_status_code_404_if_event_does_not_exist(client):
    response = client.get("/events/999999")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"

def test_get_event_returns_status_code_400_if_event_id_not_valid_integer(client):
    response = client.get("/events/abc")
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "INVALID_INPUT"
    assert response.json()["error"]["message"] == "Invalid event_id"