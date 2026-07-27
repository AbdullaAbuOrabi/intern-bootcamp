import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(name: str = "data_pipeline") -> logging.Logger:
    """
    Create and configure a logger for the ETL pipeline.
    """

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "pipeline.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate log messages
    if logger.handlers:
        return logger

    log_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Display logs in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # Save logs to a file and rotate it when it becomes large
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
