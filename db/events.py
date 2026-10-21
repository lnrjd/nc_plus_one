

def drop_events_table(cursor):
    """ DROP venues table """
    cursor.execute("DROP TABLE IF EXISTS events;")
    return


def create_events_table(cursor):
    """ CREATE events table """
    cursor.execute("""
                    CREATE TABLE events(
                        id SERIAL PRIMARY KEY
                        , title VARCHAR(255) NOT NULL
                        , description VARCHAR(255)
                        , starts_at TIMESTAMPTZ NOT NULL
                        , ends_at TIMESTAMPTZ NOT NULL
                        , organiser_id INT REFERENCES users(id)
                        , venue_id INT REFERENCES venues(id)
                        , created_at TIMESTAMPTZ DEFAULT NOW()
                    );
                    """
                   )
    return

# def normalise_event_data(event_data):
#     pass

def insert_event_data(cursor, event_data):
    """ Populate events table """
    
    insert_statement = """
                        INSERT INTO events
                            (title, description, starts_at, ends_at, organiser_id, venue_id)
                        VALUES
                            (%s, %s, %s, %s, %s, %s);
                        """

    cursor.executemany(insert_statement, [(e["title"], e["description"], e["starts_at"], e["ends_at"], e["organiser_id"], e["venue_id"]) for e in event_data])

    return


    