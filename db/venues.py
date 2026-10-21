

def drop_venues_table(cursor):
    """ DROP venues table """
    cursor.execute("DROP TABLE IF EXISTS venues;")
    return


def create_venues_table(cursor):
    """ CREATE venues table """
    cursor.execute("""
                    CREATE TABLE venues(
                        id SERIAL PRIMARY KEY
                        , name VARCHAR(255) NOT NULL
                        , address TEXT
                        , capacity INT
                    );
                    """
                   )
    return

# def normalise_venue_data(venue_data):
#     pass

def insert_venue_data(cursor, venue_data):
    """ Populate venues table """
    
    insert_statement = """
                        INSERT INTO venues
                            (name, address, capacity)
                        VALUES
                            (%s, %s, %s);
                        """

    cursor.executemany(insert_statement, [(v["name"], v["address"], v["capacity"]) for v in venue_data])

    return


    