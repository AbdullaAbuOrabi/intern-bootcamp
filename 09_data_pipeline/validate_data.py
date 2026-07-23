from pathlib import Path

import pandas as pd


# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Validation output
VALIDATION_LOG_PATH = Path(__file__).resolve().parent / "validation_log.csv"


# Raw and cleaned datasets
DATASETS = {
    "customers": {
        "raw": RAW_DATA_DIR / "customers.csv",
        "cleaned": PROCESSED_DATA_DIR / "customers_clean.parquet",
    },
    "orders": {
        "raw": RAW_DATA_DIR / "orders.csv",
        "cleaned": PROCESSED_DATA_DIR / "orders_clean.parquet",
    },
    "order_items": {
        "raw": RAW_DATA_DIR / "order_items.csv",
        "cleaned": PROCESSED_DATA_DIR / "order_items_clean.parquet",
    },
    "products": {
        "raw": RAW_DATA_DIR / "products.csv",
        "cleaned": PROCESSED_DATA_DIR / "products_clean.parquet",
    },
    "transactions": {
        "raw": RAW_DATA_DIR / "transactions.csv",
        "cleaned": PROCESSED_DATA_DIR / "transactions_clean.parquet",
    },
}


# Primary-key definitions
PRIMARY_KEYS = {
    "customers": "customer_id",
    "orders": "order_id",
    "order_items": "order_item_id",
    "products": "product_id",
    "transactions": "transaction_id",
}


# Stores every validation result
validation_results = []


def load_dataset(file_path: Path) -> pd.DataFrame:
    """Load a CSV or Parquet dataset."""

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() == ".csv":
        return pd.read_csv(file_path)

    if file_path.suffix.lower() == ".parquet":
        return pd.read_parquet(file_path)

    raise ValueError(f"Unsupported file type: {file_path.suffix}")


def add_validation_result(
    dataset: str,
    stage: str,
    check_name: str,
    status: str,
    details: str,
) -> None:
    """Add one validation result to the validation log."""

    validation_results.append(
        {
            "dataset": dataset,
            "stage": stage,
            "check_name": check_name,
            "status": status,
            "details": details,
        }
    )


def check_missing_values(
    df: pd.DataFrame,
    dataset: str,
    stage: str,
) -> None:
    """Check whether the dataset contains missing values."""

    missing_count = int(df.isna().sum().sum())

    if missing_count == 0:
        status = "PASS"
        details = "No missing values found."
    else:
        status = "FAIL"
        details = f"{missing_count} missing values found."

    add_validation_result(
        dataset=dataset,
        stage=stage,
        check_name="Missing values",
        status=status,
        details=details,
    )


def check_duplicate_rows(
    df: pd.DataFrame,
    dataset: str,
    stage: str,
) -> None:
    """Check whether the dataset contains fully duplicated rows."""

    duplicate_count = int(df.duplicated().sum())

    if duplicate_count == 0:
        status = "PASS"
        details = "No duplicate rows found."
    else:
        status = "FAIL"
        details = f"{duplicate_count} duplicate rows found."

    add_validation_result(
        dataset=dataset,
        stage=stage,
        check_name="Duplicate rows",
        status=status,
        details=details,
    )


def check_primary_key(
    df: pd.DataFrame,
    dataset: str,
    stage: str,
) -> None:
    """Check whether the primary key exists, is complete, and is unique."""

    primary_key = PRIMARY_KEYS.get(dataset)

    if primary_key is None:
        add_validation_result(
            dataset=dataset,
            stage=stage,
            check_name="Primary key validation",
            status="FAIL",
            details="No primary key configuration was found.",
        )
        return

    if primary_key not in df.columns:
        add_validation_result(
            dataset=dataset,
            stage=stage,
            check_name="Primary key validation",
            status="FAIL",
            details=f"Expected primary key '{primary_key}' was not found.",
        )
        return

    missing_count = int(df[primary_key].isna().sum())
    duplicate_count = int(df[primary_key].duplicated().sum())

    if missing_count == 0 and duplicate_count == 0:
        status = "PASS"
        details = f"Column '{primary_key}' is complete and unique."
    else:
        status = "FAIL"
        details = (
            f"Column '{primary_key}' has {missing_count} missing values "
            f"and {duplicate_count} duplicate values."
        )

    add_validation_result(
        dataset=dataset,
        stage=stage,
        check_name="Primary key validation",
        status=status,
        details=details,
    )


def check_numeric_ranges(
    df: pd.DataFrame,
    dataset: str,
    stage: str,
) -> None:
    """Check numeric business-value columns for negative values."""

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    columns_to_check = [
        column
        for column in numeric_columns
        if not column.lower().endswith("_id")
    ]

    if not columns_to_check:
        add_validation_result(
            dataset=dataset,
            stage=stage,
            check_name="Numeric range check",
            status="PASS",
            details="No numeric business-value columns required validation.",
        )
        return

    invalid_counts = {}

    for column in columns_to_check:
        negative_count = int((df[column] < 0).sum())

        if negative_count > 0:
            invalid_counts[column] = negative_count

    if not invalid_counts:
        status = "PASS"
        details = "No invalid negative numeric values found."
    else:
        problem_details = ", ".join(
            f"{column}: {count}"
            for column, count in invalid_counts.items()
        )

        status = "FAIL"
        details = f"Negative values found in {problem_details}."

    add_validation_result(
        dataset=dataset,
        stage=stage,
        check_name="Numeric range check",
        status=status,
        details=details,
    )


def check_row_count(
    raw_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    dataset: str,
) -> None:
    """Compare row counts before and after cleaning."""

    raw_count = len(raw_df)
    cleaned_count = len(cleaned_df)
    difference = raw_count - cleaned_count

    if cleaned_count <= raw_count:
        status = "PASS"
        details = (
            f"Raw rows: {raw_count}, cleaned rows: {cleaned_count}, "
            f"removed rows: {difference}."
        )
    else:
        status = "FAIL"
        details = (
            f"Cleaned data contains more rows than raw data. "
            f"Raw rows: {raw_count}, cleaned rows: {cleaned_count}."
        )

    add_validation_result(
        dataset=dataset,
        stage="raw_to_cleaned",
        check_name="Row count comparison",
        status=status,
        details=details,
    )


def check_referential_integrity(
    child_df: pd.DataFrame,
    parent_df: pd.DataFrame,
    child_column: str,
    parent_column: str,
    dataset: str,
    relationship_name: str,
) -> None:
    """Check whether foreign-key values exist in a parent dataset."""

    if child_column not in child_df.columns:
        add_validation_result(
            dataset=dataset,
            stage="cleaned",
            check_name=relationship_name,
            status="FAIL",
            details=f"Child column '{child_column}' was not found.",
        )
        return

    if parent_column not in parent_df.columns:
        add_validation_result(
            dataset=dataset,
            stage="cleaned",
            check_name=relationship_name,
            status="FAIL",
            details=f"Parent column '{parent_column}' was not found.",
        )
        return

    child_values = child_df[child_column].dropna()
    parent_values = parent_df[parent_column].dropna()

    invalid_mask = ~child_values.isin(parent_values)
    invalid_values = child_values[invalid_mask]
    invalid_count = int(invalid_values.count())

    if invalid_count == 0:
        status = "PASS"
        details = (
            f"All values in '{child_column}' exist in "
            f"the parent column '{parent_column}'."
        )
    else:
        example_values = invalid_values.drop_duplicates().head(5).tolist()

        status = "FAIL"
        details = (
            f"{invalid_count} invalid values found in '{child_column}'. "
            f"Examples: {example_values}."
        )

    add_validation_result(
        dataset=dataset,
        stage="cleaned",
        check_name=relationship_name,
        status=status,
        details=details,
    )


def validate_dataset(
    dataset: str,
    raw_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
) -> None:
    """Run standard checks for one raw and cleaned dataset."""

    check_missing_values(
        df=raw_df,
        dataset=dataset,
        stage="raw",
    )

    check_duplicate_rows(
        df=raw_df,
        dataset=dataset,
        stage="raw",
    )

    check_primary_key(
        df=raw_df,
        dataset=dataset,
        stage="raw",
    )

    check_missing_values(
        df=cleaned_df,
        dataset=dataset,
        stage="cleaned",
    )

    check_duplicate_rows(
        df=cleaned_df,
        dataset=dataset,
        stage="cleaned",
    )

    check_numeric_ranges(
        df=cleaned_df,
        dataset=dataset,
        stage="cleaned",
    )

    check_primary_key(
        df=cleaned_df,
        dataset=dataset,
        stage="cleaned",
    )

    check_row_count(
        raw_df=raw_df,
        cleaned_df=cleaned_df,
        dataset=dataset,
    )


def run_relationship_checks(
    cleaned_data: dict[str, pd.DataFrame],
) -> None:
    """Run foreign-key relationship checks between cleaned datasets."""

    required_datasets = {
        "customers",
        "orders",
        "order_items",
        "products",
        "transactions",
    }

    missing_datasets = required_datasets - cleaned_data.keys()

    if missing_datasets:
        add_validation_result(
            dataset="all_datasets",
            stage="cleaned",
            check_name="Relationship checks",
            status="FAIL",
            details=(
                "Relationship checks could not be completed. "
                f"Missing datasets: {sorted(missing_datasets)}."
            ),
        )
        return

    check_referential_integrity(
        child_df=cleaned_data["orders"],
        parent_df=cleaned_data["customers"],
        child_column="customer_id",
        parent_column="customer_id",
        dataset="orders",
        relationship_name="Orders customer integrity",
    )

    check_referential_integrity(
        child_df=cleaned_data["order_items"],
        parent_df=cleaned_data["orders"],
        child_column="order_id",
        parent_column="order_id",
        dataset="order_items",
        relationship_name="Order items order integrity",
    )

    check_referential_integrity(
        child_df=cleaned_data["order_items"],
        parent_df=cleaned_data["products"],
        child_column="product_id",
        parent_column="product_id",
        dataset="order_items",
        relationship_name="Order items product integrity",
    )

    check_referential_integrity(
        child_df=cleaned_data["transactions"],
        parent_df=cleaned_data["orders"],
        child_column="order_id",
        parent_column="order_id",
        dataset="transactions",
        relationship_name="Transactions order integrity",
    )


def save_validation_log() -> pd.DataFrame:
    """Save all validation results to a CSV file."""

    results_df = pd.DataFrame(validation_results)

    results_df.to_csv(
        VALIDATION_LOG_PATH,
        index=False,
    )

    return results_df


def run_validations() -> pd.DataFrame:
    """Load every dataset, run checks, and save the validation log."""

    validation_results.clear()
    loaded_cleaned_data = {}

    print("Starting data validation...")

    for dataset, paths in DATASETS.items():
        print(f"Validating {dataset}...")

        try:
            raw_df = load_dataset(paths["raw"])
            cleaned_df = load_dataset(paths["cleaned"])

            loaded_cleaned_data[dataset] = cleaned_df

            validate_dataset(
                dataset=dataset,
                raw_df=raw_df,
                cleaned_df=cleaned_df,
            )

        except (
            FileNotFoundError,
            ValueError,
            OSError,
            ImportError,
        ) as error:
            add_validation_result(
                dataset=dataset,
                stage="loading",
                check_name="Dataset loading",
                status="FAIL",
                details=str(error),
            )

    run_relationship_checks(loaded_cleaned_data)

    results_df = save_validation_log()

    passed_checks = int((results_df["status"] == "PASS").sum())
    failed_checks = int((results_df["status"] == "FAIL").sum())

    print("\nValidation completed.")
    print(f"Passed checks: {passed_checks}")
    print(f"Failed checks: {failed_checks}")
    print(f"Validation log saved to: {VALIDATION_LOG_PATH}")

    return results_df


if __name__ == "__main__":
    run_validations()
