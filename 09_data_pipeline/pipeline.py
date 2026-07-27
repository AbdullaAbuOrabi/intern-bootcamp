import time

from config_loader import load_config
from extract import extract_data
from transform import transform_data
from load import load_data
from logger_config import setup_logger
from summary_report import generate_summary_report
from validate_data import run_validations


logger = setup_logger()
config = load_config()


def run_pipeline() -> None:
    """Run the complete data pipeline in the correct order."""

    start_time = time.perf_counter()
    logger.info("Pipeline started.")

    try:
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

        validation_start = time.perf_counter()

        if config["validation"]["enabled"]:
            validation_results = run_validations()
        else:
            validation_results = None

        validation_duration = time.perf_counter() - validation_start

        if validation_results is not None:
            failed_checks = int(
                (validation_results["status"] == "FAIL").sum()
            )

            passed_checks = int(
                (validation_results["status"] == "PASS").sum()
            )

            validation_status = "completed"
        else:
            failed_checks = 0
            passed_checks = 0
            validation_status = "skipped"

        logger.info(
            "task=validation | status=%s | "
            "passed_checks=%d | failed_checks=%d | "
            "duration_seconds=%.4f",
            validation_status,
            passed_checks,
            failed_checks,
            validation_duration,
        )

    except Exception as error:
        logger.exception("Pipeline failed: %s", error)

        print(
            "\nALERT: The data pipeline failed. "
            "Check logs/pipeline.log for details."
        )

        raise

    total_duration = time.perf_counter() - start_time

    if config["reporting"]["generate_summary"]:
        generate_summary_report(
            transformed_data=transformed_data,
            validation_results=validation_results,
            total_duration=total_duration,
            report_path=config["paths"]["summary_report"],
        )

    logger.info(
        "Pipeline completed successfully in %.4f seconds.",
        total_duration,
    )


if __name__ == "__main__":
    run_pipeline()
