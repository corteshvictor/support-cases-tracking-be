import psycopg
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='src/.env')

def get_db_connection(dbname=None):
    conn = psycopg.connect(
        dbname=dbname or os.getenv('DB_NAME'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', 5432)
    )
    return conn

def create_database():
    db_name = os.getenv('DB_NAME')
    conn = None
    try:
        # Connect to default 'postgres' database
        conn = get_db_connection('postgres')
        conn.autocommit = True  # Allow CREATE DATABASE command to be executed
        cur = conn.cursor()

        # Check if the database already exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        exists = cur.fetchone()

        if not exists:
            cur.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully!")
        else:
            print(f"Database '{db_name}' already exists.")
        
        cur.close()
    except Exception as error:
        print(f"Error creating database: {error}")
    finally:
        if conn:
            conn.close()
