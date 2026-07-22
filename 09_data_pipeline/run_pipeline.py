import logging
import subprocess
import sys
import time
import schedule
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "pipeline_run.log"

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def run_etl_pipeline() -> bool:
    pipeline_file = BASE_DIR / "pipeline.py"

    logger.info("Starting ETL pipeline.")

    try:
        result = subprocess.run(
            [sys.executable, str(pipeline_file)],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )

        if result.stdout:
            logger.info(result.stdout.strip())

        logger.info("ETL pipeline completed successfully.")
        return True

    except subprocess.CalledProcessError as error:
        logger.error("ETL pipeline failed.")

        if error.stdout:
            logger.error("Pipeline output: %s", error.stdout.strip())

        if error.stderr:
            logger.error("Pipeline error: %s", error.stderr.strip())

        return False


def run_with_retries(max_retries: int = 3, delay_seconds: int = 5) -> bool:
    for attempt in range(1, max_retries + 1):
        logger.info("Pipeline attempt %s of %s.", attempt, max_retries)

        if run_etl_pipeline():
            return True

        if attempt < max_retries:
            logger.warning(
                "Pipeline failed. Retrying in %s seconds.",
                delay_seconds,
            )
            time.sleep(delay_seconds)

    logger.error("Pipeline failed after %s attempts.", max_retries)
    return False


def scheduled_job() -> None:
    logger.info("Scheduled pipeline run triggered.")
    run_with_retries()


if __name__ == "__main__":
    logger.info("Pipeline scheduler started.")

    scheduled_job()

    schedule.every(2).minutes.do(scheduled_job)

    logger.info("Pipeline scheduled to run every 2 minutes.")

    while True:
        schedule.run_pending()
        time.sleep(1)
