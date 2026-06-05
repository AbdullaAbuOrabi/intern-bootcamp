# Week 2 Day 5 — Data Storytelling & Mini Analytics Project

## Project Question

Which product categories generate the most revenue, and what business insights can we learn from them?

## Goal

The goal of this mini analytics project was to analyze the e-commerce dataset, create summary visuals, and explain the findings using clear business insights.

This task focused on turning analytical results into a short business story using charts, summaries, and recommendations.

## Data Used

The analysis used the e-commerce dataset from the raw CSV files:

- customers.csv
- products.csv
- orders.csv
- order_items.csv
- transactions.csv

For the main analysis, the most important files were:

- products.csv
- order_items.csv

These two files were used because the project question required product category information and sales/revenue information.

## Data Preparation

Before starting the analysis, I inspected the dataset to check:

- Column names
- Number of rows and columns
- Data types
- Missing values
- Duplicate rows

No missing values or duplicate rows were found.

The order_items table was merged with the products table using product_id.  
This connected each sold item with its product category.

## Analysis Performed

The analysis focused on three main metrics:

1. Total revenue by product category
2. Quantity sold by product category
3. Average revenue per item by product category

These metrics helped explain not only which category made the most money, but also whether the revenue came from high sales volume or high item value.

## Key Findings

### Finding 1: Books Generated the Highest Revenue

Books generated the highest total revenue with 238,604.84.  
It contributed 31.74% of total revenue.

This shows that Books was the strongest revenue-generating category in the dataset.

### Finding 2: Books Also Had the Highest Quantity Sold

Books had the highest quantity sold with 509 units.

This supports the revenue finding because Books performed well in both total revenue and sales volume.

### Finding 3: Electronics Had the Highest Average Revenue Per Item

Electronics had the highest average revenue per item at 600.15.

This means Electronics may be a high-value category, even though it did not sell as many units as Books.

## Business Recommendations

Based on the analysis, the business should:

1. Maintain strong inventory for Books because it has the highest quantity sold and total revenue.
2. Promote Electronics because it has the highest average revenue per item.
3. Review Clothing performance because it had the lowest total revenue and quantity sold.
4. Use category-level performance to guide marketing campaigns, stock planning, and product recommendations.

## Reflection on SQL and MongoDB Integration

This task connected the previous SQL and MongoDB work.

In SQL, joins and GROUP BY were used to combine tables and calculate summaries.  
In MongoDB, aggregation pipelines used stages such as $match, $lookup, $group, and $sort to summarize data.

In this notebook, pandas was used to perform similar operations:

- merge() worked like a SQL join or MongoDB $lookup
- groupby() worked like SQL GROUP BY or MongoDB $group
- sort_values() worked like SQL ORDER BY or MongoDB $sort

The main lesson is that SQL, MongoDB, and pandas can all be used to analyze data.  
The syntax is different, but the business goal is the same: turn data into useful insights.

## What I Learned

In this task, I learned how to turn analysis results into a clear business story.

I practiced:

- Loading raw CSV files
- Inspecting data quality
- Merging related tables
- Calculating business metrics
- Creating charts
- Writing insights
- Giving business recommendations

I also learned that charts alone are not enough.  
A good analytics project should explain what the numbers mean and what action the business can take.

## Deliverables

- 05_analytics/mini_project.ipynb
- 05_analytics/mini_project_report.md
- Git tag: v0.3-data-analytics