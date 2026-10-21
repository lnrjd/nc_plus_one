
import psycopg2
import os
from dotenv import load_dotenv

def get_connection():

    ENV = os.getenv("ENV", "development")
    load_dotenv(ENV)

    connection = psycopg2.connect()

    return connection

