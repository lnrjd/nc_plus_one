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

    
@pytest.fixture
def sample_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users (name, email, password_hash)
        VALUES ('user_d', 'user_d@example.com', %s)
        RETURNING id
        """,
        (hash_password("password_d"),)
    )
    user_id = cursor.fetchone()[0]
    conn.commit()
    yield user_id
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()