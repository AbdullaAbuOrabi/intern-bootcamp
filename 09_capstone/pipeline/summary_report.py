from datetime import datetime
from pathlib import Path

import pandas as pd


def generate_summary_report(
    transformed_data: dict[str, pd.DataFrame],
    validation_results: pd.DataFrame | None,
    total_duration: float,
    report_path: str,
) -> None:
    """Generate a Markdown summary for the latest pipeline run."""

    output_path = Path(report_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    passed_checks = 0
    failed_checks = 0

    if validation_results is not None:
        passed_checks = int(
            (validation_results["status"] == "PASS").sum()
        )
        failed_checks = int(
            (validation_results["status"] == "FAIL").sum()
        )

    pipeline_status = (
        "SUCCESS" if failed_checks == 0 else "COMPLETED WITH FAILURES"
    )

    report_lines = [
        "# Pipeline Run Summary",
        "",
        f"**Run date:** {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"**Pipeline status:** {pipeline_status}",
        f"**Total duration:** {total_duration:.4f} seconds",
        "",
        "## Record Counts",
        "",
        "| Dataset | Records |",
        "|---|---:|",
    ]

    for dataset_name, dataframe in transformed_data.items():
        report_lines.append(
            f"| {dataset_name} | {len(dataframe)} |"
        )

    report_lines.extend(
        [
            "",
            "## Validation Status",
            "",
            f"- Passed checks: {passed_checks}",
            f"- Failed checks: {failed_checks}",
            "",
            "## Conclusion",
            "",
            (
                "The end-to-end pipeline completed successfully and "
                "produced analytics-ready datasets."
                if failed_checks == 0
                else (
                    "The pipeline completed, but some validation checks "
                    "failed and should be reviewed."
                )
            ),
        ]
    )

    output_path.write_text(
        "\n".join(report_lines),
        encoding="utf-8",
    )

    print(f"Pipeline summary saved to: {output_path.resolve()}")
