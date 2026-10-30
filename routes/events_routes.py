from fastapi import APIRouter, HTTPException
from db.connection import get_connection
from models.events_models import select_events, select_single_event


events_router = APIRouter(prefix="/events", tags=["events"])

@events_router.get("/")
def get_events() -> dict[str, list]:
    """ Finds title, start and end times and venue information for all events ordered by start date/time.
    If two events start at the same time, they are ordered by location alphabetically

    Parameters:
    None

    Returns:
    title, start and end times, and venue name for all events as a JSON string
    """
    events = select_events()
    return {"events": events}



@events_router.get("/{event_id}")
def get_event(event_id: int) -> dict[str, dict]:
    """ Find event information for the given event_id, including:
    title, description, start and end times and venue information
    
    Parameters:
    event_id (int): id of the event to be returned

    Returns:
    event information as JSON string

    Returns status code 400 if id is not a valid integer.
    """
    event = select_single_event(event_id)

    if event is None:
        raise HTTPException(
            status_code = 404,
            detail = {"code": "NOT_FOUND", "message": "Journey not found"}
        )

    return {"event": event}