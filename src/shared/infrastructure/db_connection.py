import psycopg
from config.envs import envs

class DBConnection:
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                dbname=envs.DB_NAME,
                user=envs.DB_USER,
                password=envs.DB_PASSWORD,
                host=envs.DB_HOST,
                port=envs.DB_PORT
            )
        except psycopg.OperationalError as error:
            print(f"Error: {error}")
            self.conn.close()

    def get_connection(self):
        return self.conn

    def close_connection(self):
        self.conn.close()
