import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


print("HOST:", POSTGRES_HOST)
print("PORT:", POSTGRES_PORT)
print("DB:", POSTGRES_DB)
print("USER:", POSTGRES_USER)
print("PASSWORD LOADED:", POSTGRES_PASSWORD is not None)


database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=int(POSTGRES_PORT),
    database=POSTGRES_DB,
)

engine = create_engine(database_url)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("PostgreSQL connection successful:", result.scalar())
