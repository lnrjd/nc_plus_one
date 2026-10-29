
import os
import bcrypt
import jwt
from datetime import datetime, timezone, timedelta

ALGORITHM = "HS512"

def hash_password(password: str) -> str:
    rounds = 4 if os.getenv("ENV") == "test" else 12
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds)).decode()

def get_secret():
    return os.getenv("JWT_SECRET")


def create_access_token(id: int) -> str:
    payload = {
        "sub" : str(id)
        , "exp" : datetime.now(timezone.utc) + timedelta(minutes=60)
    }
    return jwt.encode(payload, get_secret(), algorithm=ALGORITHM)


def verify_password(password_entered, hashed_password):
    return bcrypt.checkpw(password_entered.encode(), hashed_password.encode())


