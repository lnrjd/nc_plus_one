from fastapi import APIRouter, HTTPException
from db.connection import get_connection


healthcheck_router = APIRouter(prefix="/api/health", tags=["healthcheck"])

@healthcheck_router.get("/")
def get_healthcheck():
    """
        Checks the app is alive without touching the database.

        Returns status code 200 if all is well.
    """
    return "I'm alive"