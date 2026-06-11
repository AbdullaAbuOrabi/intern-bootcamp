summary_text = f"""
# Drift Monitoring Summary Report

## Task Overview

This report summarizes the drift monitoring analysis between the training feature dataset and the recent customer feature dataset extracted from PostgreSQL.

## Datasets Compared

- Training dataset: data/processed/features.csv
- Recent dataset: customer features created from PostgreSQL tables customers, orders, and transactions

## Features Monitored

The following model input features were compared:

{', '.join(feature_columns)}

## Key Findings

The comparison showed possible drift in the following features:

{comparison_df[comparison_df["possible_drift"]].index.tolist()}

The biggest differences were found in the numeric features, especially total spent and average order amount.

## Important Observation

The training feature dataset appears to be scaled, while the recent feature dataset extracted from PostgreSQL is raw. Because of this, the large differences in numeric values may be caused by a preprocessing mismatch, not only by real business drift.

## Recommendation

The same preprocessing and scaling steps used during model training should also be applied to recent production data before prediction and monitoring. This will make the comparison more accurate and help detect real data drift more reliably.

## Output Files

- drift_comparison_metrics.csv
- drift_mean_comparison.png
- drift_total_spent_histogram.png
"""

with open(reports_dir / "drift_summary.md", "w", encoding="utf-8") as file:
    file.write(summary_text)

print("Drift summary report saved successfully.")