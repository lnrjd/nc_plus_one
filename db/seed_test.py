
from connection import get_connection
from load_data import load_json_test_data
from users import *
from venues import *
from events import *
from rsvps import *

conn = get_connection()

def seed_test(conn):

    # get data to be loaded to database
    user_data = load_json_test_data("users.json")
    venue_data = load_json_test_data("venues.json")
    event_data = load_json_test_data("events.json")
    rsvp_data = load_json_test_data("rsvps.json")

    # create tables
    with conn.cursor() as cursor:
        drop_rsvps_table(cursor)
        drop_events_table(cursor)
        drop_users_table(cursor)
        drop_venues_table(cursor)

        #create tables
        create_users_table(cursor)
        create_venues_table(cursor)
        create_events_table(cursor)
        create_rsvps_table(cursor)

        # populate tables
        insert_user_data(cursor, user_data)
        insert_venue_data(cursor, venue_data)
        insert_event_data(cursor, event_data)
        insert_rsvp_data(cursor, rsvp_data)

    conn.commit()
    return

seed_test(conn)