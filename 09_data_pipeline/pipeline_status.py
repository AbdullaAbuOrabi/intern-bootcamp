from pathlib import Path


LOG_PATH = Path("logs/pipeline.log")


def show_pipeline_status() -> None:
    """Display the latest pipeline log entries."""

    if not LOG_PATH.exists():
        print(f"Log file not found: {LOG_PATH.resolve()}")
        return

    log_lines = LOG_PATH.read_text(
        encoding="utf-8",
    ).splitlines()

    latest_lines = log_lines[-15:]

    print("\n=== Latest Pipeline Status ===\n")

    for line in latest_lines:
        print(line)


if __name__ == "__main__":
    show_pipeline_status()
