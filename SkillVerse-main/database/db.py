import psycopg2
from config import DATABASE_URL

def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn