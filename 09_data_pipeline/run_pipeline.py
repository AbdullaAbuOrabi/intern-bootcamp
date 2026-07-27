import time

from extract import extract_data
from transform import transform_data
from load import load_data
from logger_config import setup_logger


logger = setup_logger()


def run_pipeline() -> None:
    """Run the complete data pipeline in the correct order."""

    start_time = time.perf_counter()
    logger.info("Pipeline started.")

    try:
        raise RuntimeError("Test pipeline failure")

        extract_start = time.perf_counter()
        extracted_data = extract_data()
        extract_duration = time.perf_counter() - extract_start

        logger.info(
            "task=extract | status=success | duration_seconds=%.4f",
            extract_duration,
        )

        transform_start = time.perf_counter()
        transformed_data = transform_data(extracted_data)
        transform_duration = time.perf_counter() - transform_start

        logger.info(
            "task=transform | status=success | duration_seconds=%.4f",
            transform_duration,
        )

        load_start = time.perf_counter()
        load_data(transformed_data)
        load_duration = time.perf_counter() - load_start

        logger.info(
            "task=load | status=success | duration_seconds=%.4f",
            load_duration,
        )

    except Exception as error:
        logger.exception("Pipeline failed: %s", error)

        print(
            "\nALERT: The data pipeline failed. "
            "Check logs/pipeline.log for details."
        )

        raise

    total_duration = time.perf_counter() - start_time

    logger.info(
        "Pipeline completed successfully in %.4f seconds.",
        total_duration,
    )


if __name__ == "__main__":
    run_pipeline()
