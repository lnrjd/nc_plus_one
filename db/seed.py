"""
The seed function is responsible for 3 things:
    1. Removing any data from previous runs
    2. Rebuilding the table schemas
    3. Inserting the test data
"""
from load_data import load_json_data
from users import drop_users_table, create_users_table, insert_user_data

def seed(conn):

    # # get data to be inserted into database
    user_data = load_json_data("users.json")

    # drop, (re)create and populate users table
    with conn.cursor() as cursor:
        drop_users_table(cursor)
        create_users_table(cursor)
        insert_user_data(cursor, user_data)
    
    conn.commit()

    return