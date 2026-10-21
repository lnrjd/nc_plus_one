
from connection import get_connection
from load_data import load_json_data
from seed import seed

def main():

    # establish connection and create cursor
    conn = get_connection()

    #drop, (re)create and populate users table
    seed(conn)

    conn.close()

    return

main()