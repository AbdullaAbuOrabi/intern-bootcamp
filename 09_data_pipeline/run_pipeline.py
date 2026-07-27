import time

from config_loader import load_config
from logger_config import setup_logger
from pipeline import run_pipeline


logger = setup_logger()
config = load_config()


def run_with_retries() -> None:
    """Run the full pipeline with configurable retry attempts."""

    max_retries = config["pipeline"]["retries"]

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(
                "Pipeline attempt %d of %d.",
                attempt,
                max_retries,
            )

            run_pipeline()

            logger.info(
                "Pipeline orchestration completed successfully."
            )
            return

        except Exception as error:
            logger.warning(
                "Pipeline attempt %d failed: %s",
                attempt,
                error,
            )

            if attempt == max_retries:
                logger.error(
                    "Pipeline failed after %d attempts.",
                    max_retries,
                )
                raise

            wait_seconds = attempt * 2

            logger.info(
                "Retrying pipeline in %d seconds.",
                wait_seconds,
            )

            time.sleep(wait_seconds)


if __name__ == "__main__":
    run_with_retries()
