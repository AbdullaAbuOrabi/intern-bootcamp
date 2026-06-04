import logging
from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LOG_DIR = BASE_DIR / "logs"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Logging setup
# ------------------------------------------------------------

logging.basicConfig(
    filename=LOG_DIR / "pipeline_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# ------------------------------------------------------------
# Customers
# ------------------------------------------------------------

def extract_customers():
    file_path = RAW_DIR / "customers.csv"

    logging.info("Extracting customers.csv")

    customers_df = pd.read_csv(file_path)

    logging.info(f"Customers rows extracted: {len(customers_df)}")

    return customers_df


def validate_customers(customers_df):
    validation_errors = 0

    null_count = customers_df.isnull().sum().sum()
    duplicate_count = customers_df.duplicated().sum()

    if null_count > 0:
        logging.warning(f"Customers null values found: {null_count}")
        validation_errors += null_count
    else:
        logging.info("Customers: No null values found")

    if duplicate_count > 0:
        logging.warning(f"Customers duplicate rows found: {duplicate_count}")
        validation_errors += duplicate_count
    else:
        logging.info("Customers: No duplicate rows found")

    return validation_errors


def transform_customers(customers_df):
    customers_df = customers_df.copy()

    customers_df = customers_df.drop_duplicates()

    if "name" in customers_df.columns:
        customers_df["name"] = customers_df["name"].astype(str).str.title()

    if "email" in customers_df.columns:
        customers_df["email"] = customers_df["email"].astype(str).str.lower()

    if "signup_date" in customers_df.columns:
        customers_df["signup_date"] = pd.to_datetime(
            customers_df["signup_date"],
            errors="coerce"
        )

    logging.info("Customers data transformed")

    return customers_df


def load_customers(customers_df):
    output_path = PROCESSED_DIR / "customers_clean.parquet"

    customers_df.to_parquet(output_path, index=False)

    logging.info(f"Customers data saved to {output_path}")


# ------------------------------------------------------------
# Products
# ------------------------------------------------------------

def extract_products():
    file_path = RAW_DIR / "products.csv"

    logging.info("Extracting products.csv")

    products_df = pd.read_csv(file_path)

    logging.info(f"Products rows extracted: {len(products_df)}")

    return products_df


def validate_products(products_df):
    validation_errors = 0

    null_count = products_df.isnull().sum().sum()
    duplicate_count = products_df.duplicated().sum()

    if null_count > 0:
        logging.warning(f"Products null values found: {null_count}")
        validation_errors += null_count
    else:
        logging.info("Products: No null values found")

    if duplicate_count > 0:
        logging.warning(f"Products duplicate rows found: {duplicate_count}")
        validation_errors += duplicate_count
    else:
        logging.info("Products: No duplicate rows found")

    return validation_errors


def transform_products(products_df):
    products_df = products_df.copy()

    products_df = products_df.drop_duplicates()

    if "product_name" in products_df.columns:
        products_df["product_name"] = products_df["product_name"].astype(
            str).str.title()

    if "category" in products_df.columns:
        products_df["category"] = products_df["category"].astype(
            str).str.title()

    if "price" in products_df.columns:
        products_df["price"] = pd.to_numeric(
            products_df["price"], errors="coerce")

    logging.info("Products data transformed")

    return products_df


def load_products(products_df):
    output_path = PROCESSED_DIR / "products_clean.parquet"

    products_df.to_parquet(output_path, index=False)

    logging.info(f"Products data saved to {output_path}")


# ------------------------------------------------------------
# Orders
# ------------------------------------------------------------

def extract_orders():
    file_path = RAW_DIR / "orders.csv"

    logging.info("Extracting orders.csv")

    orders_df = pd.read_csv(file_path)

    logging.info(f"Orders rows extracted: {len(orders_df)}")

    return orders_df


def validate_orders(orders_df):
    validation_errors = 0

    null_count = orders_df.isnull().sum().sum()
    duplicate_count = orders_df.duplicated().sum()

    if null_count > 0:
        logging.warning(f"Orders null values found: {null_count}")
        validation_errors += null_count
    else:
        logging.info("Orders: No null values found")

    if duplicate_count > 0:
        logging.warning(f"Orders duplicate rows found: {duplicate_count}")
        validation_errors += duplicate_count
    else:
        logging.info("Orders: No duplicate rows found")

    return validation_errors


def transform_orders(orders_df):
    orders_df = orders_df.copy()

    orders_df = orders_df.drop_duplicates()

    if "order_date" in orders_df.columns:
        orders_df["order_date"] = pd.to_datetime(
            orders_df["order_date"],
            errors="coerce"
        )

    if "status" in orders_df.columns:
        orders_df["status"] = orders_df["status"].astype(str).str.lower()

    logging.info("Orders data transformed")

    return orders_df


def load_orders(orders_df):
    output_path = PROCESSED_DIR / "orders_clean.parquet"

    orders_df.to_parquet(output_path, index=False)

    logging.info(f"Orders data saved to {output_path}")


# ------------------------------------------------------------
# Order Items
# ------------------------------------------------------------

def extract_order_items():
    file_path = RAW_DIR / "order_items.csv"

    logging.info("Extracting order_items.csv")

    order_items_df = pd.read_csv(file_path)

    logging.info(f"Order items rows extracted: {len(order_items_df)}")

    return order_items_df


def validate_order_items(order_items_df):
    validation_errors = 0

    null_count = order_items_df.isnull().sum().sum()
    duplicate_count = order_items_df.duplicated().sum()

    if null_count > 0:
        logging.warning(f"Order items null values found: {null_count}")
        validation_errors += null_count
    else:
        logging.info("Order items: No null values found")

    if duplicate_count > 0:
        logging.warning(f"Order items duplicate rows found: {duplicate_count}")
        validation_errors += duplicate_count
    else:
        logging.info("Order items: No duplicate rows found")

    return validation_errors


def transform_order_items(order_items_df):
    order_items_df = order_items_df.copy()

    order_items_df = order_items_df.drop_duplicates()

    if "quantity" in order_items_df.columns:
        order_items_df["quantity"] = pd.to_numeric(
            order_items_df["quantity"],
            errors="coerce"
        )

    if "unit_price" in order_items_df.columns:
        order_items_df["unit_price"] = pd.to_numeric(
            order_items_df["unit_price"],
            errors="coerce"
        )

    if "total_price" in order_items_df.columns:
        order_items_df["total_price"] = pd.to_numeric(
            order_items_df["total_price"],
            errors="coerce"
        )

    logging.info("Order items data transformed")

    return order_items_df


def load_order_items(order_items_df):
    output_path = PROCESSED_DIR / "order_items_clean.parquet"

    order_items_df.to_parquet(output_path, index=False)

    logging.info(f"Order items data saved to {output_path}")


# ------------------------------------------------------------
# Transactions
# ------------------------------------------------------------

def extract_transactions():
    file_path = RAW_DIR / "transactions.csv"

    logging.info("Extracting transactions.csv")

    transactions_df = pd.read_csv(file_path)

    logging.info(f"Transactions rows extracted: {len(transactions_df)}")

    return transactions_df


def validate_transactions(transactions_df):
    validation_errors = 0

    null_count = transactions_df.isnull().sum().sum()
    duplicate_count = transactions_df.duplicated().sum()

    if null_count > 0:
        logging.warning(f"Transactions null values found: {null_count}")
        validation_errors += null_count
    else:
        logging.info("Transactions: No null values found")

    if duplicate_count > 0:
        logging.warning(
            f"Transactions duplicate rows found: {duplicate_count}")
        validation_errors += duplicate_count
    else:
        logging.info("Transactions: No duplicate rows found")

    return validation_errors


def transform_transactions(transactions_df):
    transactions_df = transactions_df.copy()

    transactions_df = transactions_df.drop_duplicates()

    if "transaction_date" in transactions_df.columns:
        transactions_df["transaction_date"] = pd.to_datetime(
            transactions_df["transaction_date"],
            errors="coerce"
        )

    if "amount" in transactions_df.columns:
        transactions_df["amount"] = pd.to_numeric(
            transactions_df["amount"],
            errors="coerce"
        )

    if "payment_method" in transactions_df.columns:
        transactions_df["payment_method"] = (
            transactions_df["payment_method"]
            .astype(str)
            .str.lower()
        )

    logging.info("Transactions data transformed")

    return transactions_df


def load_transactions(transactions_df):
    output_path = PROCESSED_DIR / "transactions_clean.parquet"

    transactions_df.to_parquet(output_path, index=False)

    logging.info(f"Transactions data saved to {output_path}")


# ------------------------------------------------------------
# Main Pipeline
# ------------------------------------------------------------

def run_pipeline():
    print("Pipeline started...")
    logging.info("========== Pipeline started ==========")

    total_rows_processed = 0
    total_validation_errors = 0

    # Customers
    customers_df = extract_customers()
    customer_errors = validate_customers(customers_df)
    clean_customers_df = transform_customers(customers_df)
    load_customers(clean_customers_df)

    total_rows_processed += len(clean_customers_df)
    total_validation_errors += customer_errors

    print("Customers processed")

    # Products
    products_df = extract_products()
    product_errors = validate_products(products_df)
    clean_products_df = transform_products(products_df)
    load_products(clean_products_df)

    total_rows_processed += len(clean_products_df)
    total_validation_errors += product_errors

    print("Products processed")

    # Orders
    orders_df = extract_orders()
    order_errors = validate_orders(orders_df)
    clean_orders_df = transform_orders(orders_df)
    load_orders(clean_orders_df)

    total_rows_processed += len(clean_orders_df)
    total_validation_errors += order_errors

    print("Orders processed")

    # Order Items
    order_items_df = extract_order_items()
    order_item_errors = validate_order_items(order_items_df)
    clean_order_items_df = transform_order_items(order_items_df)
    load_order_items(clean_order_items_df)

    total_rows_processed += len(clean_order_items_df)
    total_validation_errors += order_item_errors

    print("Order items processed")

    # Transactions
    transactions_df = extract_transactions()
    transaction_errors = validate_transactions(transactions_df)
    clean_transactions_df = transform_transactions(transactions_df)
    load_transactions(clean_transactions_df)

    total_rows_processed += len(clean_transactions_df)
    total_validation_errors += transaction_errors

    print("Transactions processed")

    logging.info("========== Pipeline finished ==========")
    logging.info(f"Total rows processed: {total_rows_processed}")
    logging.info(f"Total validation errors: {total_validation_errors}")

    print("Pipeline finished successfully")
    print(f"Total rows processed: {total_rows_processed}")
    print(f"Total validation errors: {total_validation_errors}")


if __name__ == "__main__":
    run_pipeline()
