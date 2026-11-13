import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_get_healthcheck_returns_status_code_200(client):
    response = client.get("/api/health")
    assert response.status_code == 200