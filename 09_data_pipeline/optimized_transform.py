import pandas as pd


def optimized_transform_data(
    extracted_data: dict[str, pd.DataFrame]
) -> dict[str, pd.DataFrame]:
    """Clean datasets while avoiding unnecessary operations."""

    transformed_data: dict[str, pd.DataFrame] = {}

    for dataset_name, dataframe in extracted_data.items():
        cleaned_dataframe = dataframe

        normalized_columns = (
            cleaned_dataframe.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )

        if not cleaned_dataframe.columns.equals(normalized_columns):
            cleaned_dataframe = cleaned_dataframe.copy()
            cleaned_dataframe.columns = normalized_columns

        if cleaned_dataframe.duplicated().any():
            cleaned_dataframe = cleaned_dataframe.drop_duplicates()

        transformed_data[dataset_name] = cleaned_dataframe

        print(
            f"Optimized transformation {dataset_name}: "
            f"{len(cleaned_dataframe)} rows"
        )

    return transformed_data
