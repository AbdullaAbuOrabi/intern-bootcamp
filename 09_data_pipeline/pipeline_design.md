# Data Pipeline Design

## Overview

This pipeline processes the e-commerce dataset through three main stages: extraction, transformation, and loading.

The goal is to create a modular, reliable, and repeatable data pipeline that prepares raw data for analytics, dashboards, reports, and machine learning.

## Pipeline Architecture

The pipeline follows this flow:

Raw CSV files → Extract → Transform → Load → Processed Parquet files → Analytics and reporting

The pipeline is controlled by `pipeline.py`, which runs the stages in the correct order.

## Pipeline Components

### extract.py

Reads the raw CSV files from `data/raw`.

It checks that every required file exists before loading it into a pandas DataFrame.

### transform.py

Cleans the extracted data.

It removes duplicate rows and standardizes column names.

### load.py

Saves the transformed datasets as Parquet files inside `data/processed`.

The same output files are replaced during every run, which prevents duplicate files and supports idempotency.

### pipeline.py

Orchestrates the full pipeline.

It runs extraction first, transformation second, and loading last.

## Reliability Principles

The pipeline is modular because each script has one clear responsibility.

It is idempotent because running it multiple times replaces the same output files instead of creating duplicates.

It also checks for missing source files and stops with an error if an input file is unavailable.

## Scalability

The current pipeline works with local CSV and Parquet files.

In the future, it could be extended to use databases, APIs, cloud storage, larger datasets, and scheduling tools such as Airflow or Prefect.

## Final Outputs

The processed datasets are stored inside `data/processed` and can be used for analytics, dashboards, reports, or machine-learning tasks.