"""
The seed function is responsible for 3 things:
    1. Removing any data from previous runs
    2. Rebuilding the table schemas
    3. Inserting the test data
"""
import os
from db.load_data import load_json_data
from db.users import *
from db.venues import *
from db.events import *
from db.rsvps import *

directory = "test_data" if os.getenv("ENV", "development") == "test" else "data"

def seed(conn):

    # get data to be loaded to database
    user_data = load_json_data("users.json", directory)
    venue_data = load_json_data("venues.json", directory)
    event_data = load_json_data("events.json", directory)
    rsvp_data = load_json_data("rsvps.json", directory)

   
    with conn.cursor() as cursor:
        # drop tables
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