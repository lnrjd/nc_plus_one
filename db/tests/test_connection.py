
from db.connection import get_connection


def test_connection_works_and_returns_empty_list_when_selecting_from_empty_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    results = cursor.fetchall()
    assert results == []