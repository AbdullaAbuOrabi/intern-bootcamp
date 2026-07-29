# Reused Components

## Data

The project will reuse these e-commerce datasets:

- data/raw/customers.csv
- data/raw/orders.csv
- data/raw/order_items.csv
- data/raw/products.csv
- data/raw/transactions.csv

## ETL Pipeline

Files from Week 9 that may be reused:

- 09_data_pipeline/extract.py
- 09_data_pipeline/transform.py
- 09_data_pipeline/load.py
- 09_data_pipeline/validate_data.py
- 09_data_pipeline/config_loader.py

These files will be copied or adapted inside the capstone `pipeline` folder.

## Machine Learning

Files from the machine-learning weeks that may be reused:

- Data preprocessing logic
- Feature engineering pipeline
- Trained reorder prediction model
- Prediction functions

These components will be placed inside the capstone `model` folder.

## Analytics

Files and logic from Week 8 that may be reused:

- KPI calculations
- Revenue analysis
- Customer analysis
- Product and category analysis
- Chart-generation logic

These components will be placed inside the capstone `analytics` folder.

## Dashboard

The Streamlit dashboard logic from Week 8 will be adapted and placed inside:

- 09_capstone/ui/

## Chatbot

The chatbot and RAG logic from Weeks 6 and 7 will be adapted and placed inside:

- 09_capstone/chatbot/

## Main Integration

The final application will connect:

Data → ETL Pipeline → Analytics → ML Predictions → Dashboard and Chatbot