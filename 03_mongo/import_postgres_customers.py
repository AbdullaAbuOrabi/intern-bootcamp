import os

import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine


def get_postgres_engine():
    """
    Connect to PostgreSQL using the credentials stored in the .env file.
    """

    load_dotenv()

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB")

    connection_string = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)
    return engine


def get_mongo_database():
    """
    Connect to MongoDB running locally.
    """

    client = MongoClient("mongodb://localhost:27017/")
    db = client["intern_db"]
    return db


def import_customers_from_postgres():
    """
    Read a small customers dataset from PostgreSQL
    and insert it into MongoDB for comparison.
    """

    postgres_engine = get_postgres_engine()
    mongo_db = get_mongo_database()

    query = """
    SELECT *
    FROM customers
    LIMIT 10;
    """

    customers_df = pd.read_sql(query, postgres_engine)

    customers_records = customers_df.to_dict(orient="records")

    mongo_db.postgres_customers.delete_many({})

    if customers_records:
        mongo_db.postgres_customers.insert_many(customers_records)

    print("PostgreSQL customers imported into MongoDB successfully.")
    print(f"Total imported records: {len(customers_records)}")


if __name__ == "__main__":
    import_customers_from_postgres()
