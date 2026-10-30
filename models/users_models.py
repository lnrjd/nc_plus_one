from db.connection import get_connection
from utils.utils import hash_password

def get_user_from_email(email: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * 
            FROM users
            WHERE email = %s;
        """
        , (email,)
    )
    user = cursor.fetchone()

    if user is None:
        return user

    cursor.close()
    conn.close()
    return {
            "id": user[0]
            , "email": user[1]
            , "password_hash": user[2]
            , "name": user[3]
            , "created_at": user[4]
        }



def insert_new_user(name:str, email: str, password: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    
    if get_user_from_email(email) is not None:
        return None
    
    cursor.execute(
        """
            INSERT INTO users (name, email, password_hash)
            VALUES (%s, %s, %s)
            RETURNING *;
        """
        , (name, email, hash_password(password))
    )
    new_user = cursor.fetchone()

    cursor.close()
    conn.close()
    return {
            "id": new_user[0]
            , "name": new_user[3]
            , "email": new_user[1]
            , "created_at": new_user[4]
        }