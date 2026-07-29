# Customer Insights and Sales Analytics Assistant

## Project Overview

This project is an end-to-end data product that combines data engineering, analytics, machine learning, and GenAI.

The application will process e-commerce data, calculate business insights, predict customer reordering behavior, and present the results through an interactive dashboard and chatbot.

## Problem Statement

Businesses may have large amounts of customer, order, product, and transaction data, but it can be difficult to understand the data manually.

This project will automate the process of cleaning, analyzing, and presenting the data so that business users can easily understand sales performance and customer behavior.

## Project Goal

The goal is to build a complete application that:

- Processes raw e-commerce data through an ETL pipeline.
- Calculates important sales and customer KPIs.
- Predicts whether customers are likely to reorder.
- Displays insights through a Streamlit dashboard.
- Allows users to ask business questions through a chatbot.

## Input Data

The project will use the following datasets:

- customers.csv
- orders.csv
- order_items.csv
- products.csv
- transactions.csv

## Expected Outputs

The system will produce:

- Cleaned and processed datasets.
- Sales and customer KPIs.
- Customer reorder predictions.
- Interactive charts and filters.
- Chatbot answers based on business data.

## Project Architecture

The application will follow this flow:

Raw Data → ETL Pipeline → Processed Data → Analytics and Machine Learning → Dashboard and Chatbot

## Tools and Technologies

- Python
- pandas
- PostgreSQL or processed Parquet files
- scikit-learn
- Streamlit
- LangChain or a simple chatbot workflow
- Matplotlib or Plotly