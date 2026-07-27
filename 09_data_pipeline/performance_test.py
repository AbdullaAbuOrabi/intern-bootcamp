import csv
import time
from pathlib import Path

from extract import extract_data
from transform import transform_data
from load import load_data
from optimized_transform import optimized_transform_data


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "performance_results.csv"
NUMBER_OF_RUNS = 5


def measure_transform(
    extracted_data,
    transform_function,
) -> float:
    """Measure one transformation function."""

    start_time = time.perf_counter()
    transform_function(extracted_data)
    return time.perf_counter() - start_time


def compare_transformations() -> None:
    """Compare average runtime of original and optimized transforms."""

    extracted_data = extract_data()

    original_times = []
    optimized_times = []

    for run_number in range(1, NUMBER_OF_RUNS + 1):
        print(f"\nPerformance test run {run_number} of {NUMBER_OF_RUNS}")

        original_duration = measure_transform(
            extracted_data,
            transform_data,
        )
        original_times.append(original_duration)

        optimized_duration = measure_transform(
            extracted_data,
            optimized_transform_data,
        )
        optimized_times.append(optimized_duration)

    original_average = sum(original_times) / NUMBER_OF_RUNS
    optimized_average = sum(optimized_times) / NUMBER_OF_RUNS

    improvement_percentage = (
        (original_average - optimized_average)
        / original_average
        * 100
    )

    results = [
        [
            "version",
            "average_transform_seconds",
            "number_of_runs",
        ],
        [
            "before_optimization",
            round(original_average, 6),
            NUMBER_OF_RUNS,
        ],
        [
            "after_optimization",
            round(optimized_average, 6),
            NUMBER_OF_RUNS,
        ],
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(results)

    print("\nPerformance comparison complete.")
    print(f"Original average: {original_average:.6f} seconds")
    print(f"Optimized average: {optimized_average:.6f} seconds")
    print(f"Improvement: {improvement_percentage:.2f}%")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    compare_transformations()
