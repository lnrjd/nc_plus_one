from db.connection import get_connection

def select_events() -> list[dict]:
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
            ORDER BY e.starts_at, location;
        """
    )
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [dict(zip(columns,row)) for row in rows]


def select_single_event(event_id: int):
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
    event = cursor.fetchone()
    cursor.close()
    conn.close()
   
    if event is None:
            return None
    
    return {
                "id": event[0]
                , "title": event[1]
                , "description": event[2]
                , "starts_at": event[3]
                , "ends_at": event[4]
                , "location": event[5]
                , "address": event[6]
                , "capacity": event[7]
                , "created_at": event[8]
            }
