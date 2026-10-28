import sys

sys.path.append("../nc_plus_one")

from utils.utils import hash_password

def drop_users_table(cursor):
    """ DROP users table """
    cursor.execute("DROP TABLE IF EXISTS users;")
    return


def create_users_table(cursor):
    """ CREATE users table """
    cursor.execute("""
                    CREATE TABLE users(
                        id SERIAL PRIMARY KEY
                        , email VARCHAR(255) UNIQUE NOT NULL
                        , password_hash VARCHAR(255) NOT NULL
                        , name VARCHAR(255) NOT NULL
                        , created_at TIMESTAMPTZ DEFAULT NOW()
                    );
                    """
                   )
    return

# def normalise_user_data(user_data):
#     pass

def insert_user_data(cursor, user_data):
    """ Populate users table with data from users.json file """
    
    insert_statement = """
                        INSERT INTO users
                            (name, email, password_hash)
                        VALUES
                            (%s, %s, %s);
                        """

    cursor.executemany(insert_statement, [(u["name"], u["email"], hash_password(u["password"])) for u in user_data])

    return


    