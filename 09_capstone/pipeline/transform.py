import pandas as pd


def transform_data(
    extracted_data: dict[str, pd.DataFrame]
) -> dict[str, pd.DataFrame]:
    """Clean and prepare the extracted e-commerce datasets."""

    transformed_data: dict[str, pd.DataFrame] = {}

    for dataset_name, dataframe in extracted_data.items():
        cleaned_dataframe = dataframe.copy()

        # Remove duplicate rows.
        cleaned_dataframe = cleaned_dataframe.drop_duplicates()

        # Remove spaces from column names.
        cleaned_dataframe.columns = (
            cleaned_dataframe.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        transformed_data[dataset_name] = cleaned_dataframe

        print(
            f"Transformed {dataset_name}: "
            f"{len(cleaned_dataframe)} rows"
        )

    return transformed_data
