from pathlib import Path

import pandas as pd


PROCESSED_DATA_PATH = (
    Path(__file__).resolve().parent.parent / "data" / "processed"
)


def load_data(
    transformed_data: dict[str, pd.DataFrame]
) -> None:
    """Save transformed datasets as Parquet files."""

    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    for dataset_name, dataframe in transformed_data.items():
        output_path = (
            PROCESSED_DATA_PATH / f"{dataset_name}_clean.parquet"
        )

        dataframe.to_parquet(output_path, index=False)

        print(
            f"Loaded {dataset_name}: "
            f"{output_path}"
        )
