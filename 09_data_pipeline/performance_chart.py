from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
RESULTS_FILE = BASE_DIR / "performance_results.csv"
OUTPUT_FILE = BASE_DIR / "performance_comparison.png"


def create_performance_chart() -> None:
    """Create a chart comparing transformation performance."""

    results = pd.read_csv(RESULTS_FILE)

    plt.figure(figsize=(8, 5))

    plt.bar(
        results["version"],
        results["average_transform_seconds"],
    )

    plt.title("Transformation Performance Comparison")
    plt.xlabel("Pipeline Version")
    plt.ylabel("Average Transform Time (Seconds)")

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=300)
    plt.close()

    print(f"Performance chart saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_performance_chart()
