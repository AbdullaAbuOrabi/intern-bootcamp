

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="intern_db",
    user="postgres",
    password="Abdulla11-11"
)

print("PostgreSQL connected successfully!")

conn.close()
