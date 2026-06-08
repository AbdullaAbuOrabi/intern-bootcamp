# Day 4 — Exploratory Data Analysis (EDA)

## Learning Focus

In this task, I practiced Exploratory Data Analysis using pandas, matplotlib, and seaborn.

The goal of EDA is to understand the data before making decisions. I used the cleaned datasets to find patterns, trends, relationships, and possible outliers.

## What I Completed

I created a Jupyter notebook called:

`05_analytics/eda_analysis.ipynb`

Inside the notebook, I loaded the cleaned customer, product, order, order item, and transaction datasets from the processed data folder.

I used pandas to inspect the data, check the structure, calculate descriptive statistics, and understand the columns.

I also created a main analysis table called `sales` by joining order items, orders, products, and customers together.

## Visualizations Created

I created the following visualizations:

1. Revenue over time  
2. Top 10 customers by revenue  
3. Revenue by product category  
4. Boxplot of order item total price  
5. Correlation heatmap for numeric variables  

## What I Learned

I learned that EDA is used to explore and understand data before creating dashboards, reports, or machine learning models.

I learned how to use pandas to load data, inspect rows and columns, calculate descriptive statistics, and group data to answer business questions.

I learned how to use matplotlib and seaborn to create clear visualizations.

I also learned how boxplots can help detect outliers and how correlation heatmaps can show relationships between numeric variables.

## Key Findings

Revenue changed across different order dates, meaning some days performed better than others.

Some customers generated more revenue than others, which helps identify valuable customers.

Some product categories contributed more revenue than others.

The boxplot showed that some order item values may be unusually high compared to the rest of the data.

The correlation heatmap showed the relationship between quantity, unit price, and total price.

## Final Result

By the end of this task, I completed an EDA notebook with meaningful visualizations and summarized the findings in a markdown report.

This task helped me understand how data analysis turns cleaned data into business insights.
