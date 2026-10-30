import os
import sys
import jwt
from models.users_models import get_user_from_email
from utils.utils import hash_password

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient

from main import app

def test_login_returns_status_code_200_for_valid_user(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_d@example.com", "password": "password_d"})
    assert response.status_code == 200

def test_login_returns_token_for_valid_user(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_d@example.com", "password": "password_d"})
    assert response.json()["access_token"] is not None

def test_login_returns_token_payload_includes_user_id_and_expiry(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_d@example.com", "password": "password_d"})
    token = response.json()["access_token"]
    ALGORITHM = "HS512"
    secret = os.getenv("JWT_SECRET")
    decoded_token = jwt.decode(response.json()["access_token"], algorithms=ALGORITHM, key=secret)
    assert int(decoded_token["sub"]) is not None
    assert int(decoded_token["exp"]) is not None
    
def test_login_returns_400_if_email_missing(client, sample_user):
    response = client.post("/auth/login", json={"email": "", "password": "password_d"})
    assert response.status_code == 400

def test_login_returns_400_if_password_missng(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_d@example.com", "password": ""})
    assert response.status_code == 400

def test_login_returns_401_if_email_not_found(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_z@example.com", "password": "password_d"})
    assert response.status_code == 401

def test_login_returns_401_if_password_incorrect(client, sample_user):
    response = client.post("/auth/login", json={"email": "user_d@example.com", "password": "password_z"})
    assert response.status_code == 401

def test_login_returns_same_error_if_email_not_found_or_password_incorrect(client, sample_user):
    response_1 = client.post("/auth/login", json={"email": "user_z@example.com", "password": "password_d"})
    response_2 = client.post("/auth/login", json={"email": "user_d@example.com", "password": "password_z"})
    assert response_1.status_code == response_2.status_code
    assert response_1.json()["error"] == response_2.json()["error"]







def test_register_returns_201_for_valid_input(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_z", "email": "user_z@example.com", "password": "password_z"})
    assert response.status_code == 201

def test_register_creates_returns_new_user_info_for_valid_input(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_z", "email": "user_z@example.com", "password": "password_z"})
    assert response.json()["user"]["name"] == "user_z"
    assert response.json()["user"]["email"] == "user_z@example.com"

def test_register_response_returns_user_with_no_password_included(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_z", "email": "user_z@example.com", "password": "password_z"})
    assert "password" not in response.json()["user"]

def test_register_returns_409_status_code_if_email_already_registered(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_a", "email": "user_a@example.com", "password": "password_a"})
    assert response.status_code == 409

def test_register_returns_400_status_code_if_name_missing(client, re_seed_database):
    response = client.post("/auth/register", json={"name": None, "email": "user_z@example.com", "password": "password_z"})
    assert response.status_code == 400

def test_register_returns_400_status_code_if_email_missing(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_z", "email": None, "password": "password_z"})
    assert response.status_code == 400

def test_register_returns_400_status_code_if_password_missing(client, re_seed_database):
    response = client.post("/auth/register", json={"name": "user_z", "email": "user_z@example.com", "password": None})
    assert response.status_code == 400





