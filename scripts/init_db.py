from db_connection import get_db_connection, create_database
from create_tables import create_tables
from insert_data import insert_sample_data

def execute_sql_commands(commands):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
        print("Commands executed successfully!")
    except Exception as error:
        print(f"Error executing commands: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()
    execute_sql_commands(create_tables())
    execute_sql_commands(insert_sample_data())
