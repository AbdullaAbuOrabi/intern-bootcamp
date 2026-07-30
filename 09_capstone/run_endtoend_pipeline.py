import logging

from pipeline.pipeline import run_pipeline
from model.batch_predict import run_batch_prediction


logger = logging.getLogger("data_pipeline")


def run_endtoend_pipeline() -> None:
    """Run the ETL pipeline, then generate customer predictions."""

    logger.info("End-to-end capstone pipeline started.")

    try:
        run_pipeline()

        logger.info("ETL pipeline completed successfully.")

        run_batch_prediction()

        logger.info("Machine-learning predictions completed successfully.")
        logger.info("End-to-end capstone pipeline completed successfully.")

    except Exception as error:
        logger.exception(
            "End-to-end capstone pipeline failed: %s",
            error,
        )
        raise


if __name__ == "__main__":
    run_endtoend_pipeline()
