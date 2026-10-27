from fastapi import APIRouter, HTTPException
from db.connection import get_connection


events_router = APIRouter(prefix="/events", tags=["events"])

@events_router.get("/")
def get_events():
    """ Returns all events ordered by start date/time.
    If two events start at the same time, order by location alphabetically
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
            """
            SELECT
                e.id
                , e.title
                , e.starts_at
                , e.ends_at
                , v.name as location
            FROM events e
            INNER JOIN venues v ON e.venue_id = v.id
            ORDER BY e.starts_at, location
            """
        )

    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"events": [dict(zip(columns,row)) for row in rows]}


@events_router.get("/{event_id}")
def get_event(event_id: int):
    """ Returns single event by id, including venue information.
    Returns status code 400 if id is not a valid integer.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
            """
            SELECT
                e.id
                , e.title
                , e.description
                , e.starts_at
                , e.ends_at
                , v.name as location
                , v.address
                , v.capacity
                , e.created_at
            FROM events e
            INNER JOIN venues v ON e.venue_id = v.id
            WHERE e.id = %s
            """,
            (event_id,)
        )
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        raise HTTPException(
            status_code = 404,
            detail = {"code": "NOT_FOUND", "message": "Journey not found"}
        )

    return {"event": {
                "id": row[0]
                , "title": row[1]
                , "description": row[2]
                , "starts_at": row[3]
                , "ends_at": row[4]
                , "location": row[5]
                , "address": row[6]
                , "capacity": row[7]
                , "created_at": row[8]
            }
        }