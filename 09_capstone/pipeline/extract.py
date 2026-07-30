from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "raw"

FILE_NAMES = {
    "customers": "customers.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "products": "products.csv",
    "transactions": "transactions.csv",
}


def extract_data() -> dict[str, pd.DataFrame]:
    """Read all raw e-commerce CSV files and return them as DataFrames."""
    extracted_data: dict[str, pd.DataFrame] = {}

    for dataset_name, file_name in FILE_NAMES.items():
        file_path = RAW_DATA_PATH / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"Missing input file: {file_path}")

        extracted_data[dataset_name] = pd.read_csv(file_path)
        print(
            f"Extracted {dataset_name}: "
            f"{len(extracted_data[dataset_name])} rows"
        )

    return extracted_data


if __name__ == "__main__":
    extract_data()
