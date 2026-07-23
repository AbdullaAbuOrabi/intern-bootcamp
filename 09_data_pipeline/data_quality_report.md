# Data Quality and Validation Report

## Overview

This task focused on validating the raw and cleaned datasets used in the data pipeline. The goal was to confirm that the data is complete, consistent, correctly structured, and reliable before being used for analysis or other processes.

## Datasets Validated

The following datasets were checked:

- Customers
- Orders
- Order items
- Products
- Transactions

## Validation Checks

The validation script checked:

- Missing values
- Duplicate rows
- Primary key completeness and uniqueness
- Invalid negative numeric values
- Row count differences between raw and cleaned data
- Referential integrity between related datasets

Examples of relationship checks included:

- Every customer in the orders dataset exists in the customers dataset.
- Every order in the order items dataset exists in the orders dataset.
- Every product in the order items dataset exists in the products dataset.
- Every transaction is connected to an existing order.

## Validation Results

The validation process completed successfully.

- Passed checks: 44
- Failed checks: 0

All datasets passed the required validation checks. No missing values, duplicate primary keys, invalid negative values, or broken dataset relationships were detected.

The full validation results were saved in:

`09_data_pipeline/validation_log.csv`

## What I Learned

I learned that cleaning data and validating data are two different steps. The pipeline transforms and prepares the data, while validation checks confirm that the final data is accurate and trustworthy. I also learned how to automate quality checks using pandas, validate relationships between datasets, detect anomalies, and save validation results in a separate log file.

## Conclusion

The data validation script was completed successfully. All 44 checks passed, which confirms that the cleaned datasets are consistent, properly connected, and ready for further analysis or processing.