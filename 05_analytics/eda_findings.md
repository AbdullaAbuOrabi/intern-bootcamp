# EDA Deep Dive Findings

## Task Overview

This analysis focused on performing a deeper exploratory data analysis on the e-commerce dataset. The goal was to understand sales performance, product performance, customer behavior, and order value patterns using cleaned and structured data.

The analysis used customer, order, product, order item, and transaction data to create a combined EDA dataset for business insights.

## Data Preparation

The raw CSV files were loaded into pandas DataFrames. The datasets included customers, orders, order items, products, and transactions.

Date columns such as signup date, order date, and transaction date were converted into datetime format to support time-based analysis.

The separate tables were merged into one main EDA dataset so that customer, order, product, and payment information could be analyzed together.

## Business Summary

The dataset contained 200 orders, 86 active customers, 30 products, and 1513 total items sold.

The raw total revenue was 751,781.25. However, after filtering only completed orders with paid payment status, the confirmed revenue was 84,010.91 from 23 confirmed orders.

This shows that many orders were cancelled, pending, failed, or refunded, so confirmed sales are more reliable for business analysis.

## Key Findings

### 1. Daily Confirmed Revenue

Confirmed revenue changed across different days. Some days showed strong revenue spikes, while other days had much lower confirmed sales.

This means the business should monitor daily revenue trends and investigate what causes high-performing days.

### 2. Revenue by Product Category

The Home category generated the highest confirmed revenue, followed by Clothing, Electronics, and Books.

Books had the highest quantity sold, but it did not generate the highest revenue. This suggests that Books may have lower prices, while Home products may generate more revenue per sale.

### 3. Top Products

Product23, Product22, and Product11 were the strongest products by confirmed revenue.

These products should be prioritized for stock planning, marketing, and product promotion because they contribute strongly to successful sales.

### 4. Customer Spending

Most customers had moderate confirmed spending, while a smaller number of customers spent much more.

These high-value customers are important and could be targeted with loyalty offers, personalized promotions, or retention campaigns.

### 5. Order Value Distribution

Most confirmed orders were within a normal value range, but a few orders had much higher values.

These high-value orders can strongly affect total revenue and average order value, so they should be reviewed to understand which customers or products created them.

## Conclusion

The analysis shows that the business should focus on confirmed successful sales instead of raw total order value.

The most important insights are that Home is the strongest revenue category, Product23 is the top product, and a small number of customers and orders contribute strongly to revenue.

These findings can be used later to design an analytics dashboard that focuses on revenue trends, category performance, top products, customer value, and order behavior.