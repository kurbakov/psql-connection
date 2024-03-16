import psycopg2

# auth credentials
USER = "postgres"
PASS = "postgres"

# Postgres location
HOST = "127.0.0.1"
PORT = "5432"

# Postgres DB
DB = "postgres"

def test_connection():
    print("Connecting to the database...")

    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASS,
            host=HOST,
            port=PORT,
            database=DB
        )

        cursor = connection.cursor()
        print("Database connection successful")

    except Exception as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            print("Executing select on open connection to make sure conneciton is 100% functionsl...")
            cursor.execute("SELECT * FROM pg_catalog.pg_tables;")
            publisher_records = cursor.fetchall()
            print("Received data from query:")
            print(publisher_records)

            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    test_connection()
