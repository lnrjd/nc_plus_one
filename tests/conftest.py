import os
import pytest
from fastapi.testclient import TestClient
from main import app
from db.connection import get_connection
from utils.utils import hash_password


os.environ["ENV"] = "test"

@pytest.fixture
def client():
    return TestClient(app)

    
