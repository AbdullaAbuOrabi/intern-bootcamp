from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline() -> None:
    """Run the complete data pipeline in the correct order."""

    print("Starting pipeline...")

    try:
        extracted_data = extract_data()
        transformed_data = transform_data(extracted_data)
        load_data(transformed_data)

    except Exception as error:
        print(f"Pipeline failed: {error}")
        raise

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
