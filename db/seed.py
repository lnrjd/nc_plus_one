"""
The seed function is responsible for 3 things:
    1. Removing any data from previous runs
    2. Rebuilding the table schemas
    3. Inserting the test data
"""
from load_data import load_json_data
from users import drop_users_table, create_users_table, insert_user_data
from venues import drop_venues_table, create_venues_table, insert_venue_data

def seed(conn):

    # get data to be inserted into database
    user_data = load_json_data("users.json")
    venue_data = load_json_data("venues.json")

   
    with conn.cursor() as cursor:
        # drop tables
        drop_users_table(cursor)
        drop_venues_table(cursor)

        #create tables
        create_users_table(cursor)
        create_venues_table(cursor)

        # populate tables
        insert_user_data(cursor, user_data)
        insert_venue_data(cursor, venue_data)
    
    conn.commit()

    return