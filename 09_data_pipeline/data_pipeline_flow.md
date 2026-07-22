# E-commerce Data Pipeline Architecture

```mermaid
flowchart TD
    A[Raw CSV Files] --> B[extract.py]
    B --> C[Raw DataFrames]
    C --> D[transform.py]
    D --> E[Cleaned DataFrames]
    E --> F[load.py]
    F --> G[Parquet Files in data/processed]
    G --> H[Analytics, Dashboards, Reports, and ML]

    I[pipeline.py] --> B
    I --> D
    I --> F