

def drop_rsvps_table(cursor):
    """ DROP rsvps table """
    cursor.execute("DROP TABLE IF EXISTS rsvps;")
    return


def create_rsvps_table(cursor):
    """ CREATE rsvps table """
    cursor.execute("""
                    CREATE TABLE rsvps(
                        id SERIAL PRIMARY KEY
                        , attendee_id INT REFERENCES users(id)
                        , event_id INT REFERENCES events(id)
                        , created_at TIMESTAMPTZ DEFAULT NOW()
                    );
                    """
                   )
    return

# def normalise_rsvp_data(rsvp_data):
#     pass

def insert_rsvp_data(cursor, rsvp_data):
    """ Populate rsvps table with data from rsvps.json file """
    
    insert_statement = """
                        INSERT INTO rsvps
                            (attendee_id, event_id)
                        VALUES
                            (%s, %s);
                        """

    cursor.executemany(insert_statement, [(r["attendee_id"], r["event_id"]) for r in rsvp_data])

    return


    