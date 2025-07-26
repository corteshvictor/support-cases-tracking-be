import psycopg
from config.envs import envs

class DBConnection:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg.connect(
                dbname=envs.DB_NAME,
                user=envs.DB_USER,
                password=envs.DB_PASSWORD,
                host=envs.DB_HOST,
                port=envs.DB_PORT,
            )
        except psycopg.OperationalError as error:
            # Avoid referencing self.conn if the connection was not created
            print(f"Error: {error}")

    def get_connection(self):
        if not self.conn:
            raise ConnectionError("Database connection not established")
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
