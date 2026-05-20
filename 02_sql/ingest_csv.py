import logging
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Load database credentials from .env
load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# CSV folder path
RAW_DATA_PATH = Path("data/raw")


# Expected columns for validation
EXPECTED_COLUMNS = {
    "customers": [
        "customer_id",
        "first_name",
        "email",
        "city",
        "signup_date"
    ],
    "products": [
        "product_id",
        "product_name",
        "category",
        "price"
    ],
    "orders": [
        "order_id",
        "customer_id",
        "order_date",
        "status"
    ],
    "order_items": [
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "total_price"
    ],
    "transactions": [
        "transaction_id",
        "order_id",
        "payment_method",
        "payment_status",
        "transaction_date",
        "amount"
    ]
}


def create_postgres_engine():
    """Create a SQLAlchemy connection engine for PostgreSQL."""
    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=int(POSTGRES_PORT),
        database=POSTGRES_DB,
    )

    return create_engine(database_url)


def validate_dataframe(df, table_name):
    """Validate dataframe columns, null values, and duplicate rows."""
    logging.info(f"Validating table: {table_name}")

    expected_columns = EXPECTED_COLUMNS[table_name]

    missing_columns = set(expected_columns) - set(df.columns)
    extra_columns = set(df.columns) - set(expected_columns)

    if missing_columns:
        raise ValueError(f"{table_name} is missing columns: {missing_columns}")

    if extra_columns:
        logging.warning(f"{table_name} has extra columns: {extra_columns}")

    null_count = df.isnull().sum().sum()
    duplicate_count = df.duplicated().sum()

    logging.info(f"{table_name}: null values found: {null_count}")
    logging.info(f"{table_name}: duplicate rows found: {duplicate_count}")

    if duplicate_count > 0:
        df = df.drop_duplicates()
        logging.info(f"{table_name}: duplicate rows removed")

    return df


def ingest_csv_file(engine, table_name):
    """Read one CSV file, validate it, and load it into PostgreSQL."""
    file_path = RAW_DATA_PATH / f"{table_name}.csv"

    logging.info(f"Reading file: {file_path}")

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    df = validate_dataframe(df, table_name)

    logging.info(f"Loading {table_name} into PostgreSQL")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    logging.info(f"{table_name} loaded successfully. Rows inserted: {len(df)}")


def main():
    """Run the full CSV ingestion process."""
    logging.info("Starting CSV ingestion process")

    engine = create_postgres_engine()

    tables = [
        "customers",
        "products",
        "orders",
        "order_items",
        "transactions"
    ]

    for table_name in tables:
        ingest_csv_file(engine, table_name)

    logging.info("CSV ingestion process completed successfully")


if __name__ == "__main__":
    main()
