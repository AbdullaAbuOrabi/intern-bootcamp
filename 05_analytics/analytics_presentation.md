# Mini Analytics Project and Presentation

## Task Overview

The purpose of this task was to combine data analysis, KPI measurement, visualization, dashboard development, and business storytelling into one complete mini analytics project.

The project focused on customer purchase behavior and sales performance. Customer, order, order-item, product, and transaction data were combined to analyze confirmed revenue, successful orders, product performance, customer behavior, payment outcomes, and business improvement opportunities.

## Project Objective

The objective was to understand what factors drive successful sales and identify areas where the business could improve.

The project answered questions such as:

- How does confirmed revenue change over time?
- Which product categories generate the most revenue?
- Which individual products perform best?
- Which customer cities generate the most revenue?
- How successful are customer payments?
- How many customers return to purchase again?

## Data Used

The project used the following cleaned datasets:

- Customers
- Orders
- Order items
- Products
- Transactions

These datasets were merged using `customer_id`, `order_id`, and `product_id` to create one complete analytics dataset.

Only orders that were both completed and successfully paid were used for confirmed revenue analysis.

## Tools and Libraries Used

The project was completed using:

- Python
- Pandas
- Plotly
- Jupyter Notebook
- Streamlit
- VS Code
- Markdown

## Main KPIs

The main business KPIs were:

- Confirmed Revenue: **84,010.91**
- Successful Orders: **23**
- Successful Order Rate: **11.50%**
- Average Order Value: **3,652.65**
- Total Items Sold: **177**
- Successful Customers: **20**
- Returning Customer Rate: **15.00%**
- Payment Success Rate: **33.50%**

## Main Findings

The business generated **84,010.91** in confirmed revenue from **23 orders** that were both completed and successfully paid.

Daily revenue was not stable during the analysis period. The highest daily confirmed revenue was **9,378.07 on 10 May 2026**, while the lowest was **203.10 on 15 April 2026**.

The **Home** category generated the highest confirmed revenue at **25,510.71**, while Books generated the lowest category revenue.

The strongest individual products were **Product23**, **Product22**, and **Product11**.

Abu Dhabi generated the highest confirmed revenue at **26,582.41**, followed closely by Ajman at **26,091.77**.

Payment performance was one of the main business problems. Only **67 transactions were paid**, while **62 failed** and **71 were refunded**.

Customer retention was also low. Out of 20 successful customers, only 3 returned to make another successful purchase.

## Business Recommendations

The business should investigate the causes of failed and refunded transactions to improve the payment success rate.

Loyalty rewards, follow-up offers, and personalized recommendations could help increase repeat purchases and improve customer retention.

The business should maintain good product availability for the strongest categories and highest-performing products.

Marketing efforts could focus more on Abu Dhabi and Ajman, where confirmed revenue was highest.

The company should also investigate the strongest revenue days to understand whether particular products, customers, promotions, or activities caused the increase.

## Dashboard Presentation

A Streamlit dashboard was created to present the final results.

The dashboard includes:

- Executive KPI cards
- Daily confirmed revenue trend
- Revenue by product category
- Top products by confirmed revenue
- Revenue by customer city
- Payment outcome analysis
- Customer-retention analysis
- Business recommendations
- Final conclusion

Each chart includes a section explaining what the chart shows, what the result means, and what action the business could take.

## What I Learned

In this task, I learned how to combine the different analytics skills from the previous tasks into one complete project. I used data preparation, KPI calculations, visualizations, and Streamlit dashboard development together. The most important new skill was learning how to interpret charts instead of only creating them. For every chart, I identified the business question it answered, explained the main result, described why the result mattered, and suggested a possible business action. I also learned that a good analytics presentation should follow a clear story and should only include charts that support useful business decisions.

## Deliverables

The completed deliverables are:

- `05_analytics/mini_analytics_project.ipynb`
- `05_analytics/mini_analytics_dashboard.py`
- `05_analytics/analytics_presentation.md`

## Conclusion

This task brought together all the work completed during Week 8. The final project transformed cleaned data into KPIs, charts, business insights, recommendations, and an interactive presentation dashboard.

The analysis showed that the strongest opportunities come from the best-performing products, categories, and cities. However, payment performance and customer retention need improvement. Addressing these areas could help the business achieve more stable and sustainable revenue.