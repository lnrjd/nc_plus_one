from fastapi import APIRouter
from db.connection import get_connection


events_router = APIRouter(prefix="/events", tags=["events"])

@events_router.get("/")
def get_events():
    """ Returns all events ordered by start date/time.
    If two events start at teh same time, order by location alphabetically
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