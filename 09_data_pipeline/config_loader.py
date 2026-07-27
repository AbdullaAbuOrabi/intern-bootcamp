from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"


def load_config() -> dict[str, Any]:
    """Load and return the pipeline configuration."""

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file was not found: {CONFIG_PATH}"
        )

    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    if not config:
        raise ValueError("The configuration file is empty.")

    return config
