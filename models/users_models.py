from db.connection import get_connection

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