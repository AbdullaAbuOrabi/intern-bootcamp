# Business Metrics Summary

## Task Overview

In this task, I designed and calculated key business performance indicators using the customer, order, order item, product, and transaction datasets.

The goal was to move from raw data into useful business metrics that can help explain performance. The KPIs were calculated using Python and then validated using SQL queries to make sure the results were correct.

## KPIs Calculated

| KPI | Value | Meaning |
|---|---:|---|
| Total Revenue | AED 84,010.91 | Revenue from completed and paid orders |
| Successful Orders | 23 | Orders that were both completed and paid |
| Successful Order Rate | 11.5% | Percentage of all orders that became successful |
| Average Order Value | AED 3,652.65 | Average revenue per successful order |
| Returning Customer Rate | 15% | Percentage of successful customers who ordered more than once |
| Total Items Sold | 177 | Total items sold in successful orders |
| Payment Success Rate | 33.5% | Percentage of transactions with paid status |

## KPI Rules

For this task, an order was counted as successful only when:

- Order status = completed
- Payment status = paid

This rule was used because cancelled, pending, failed, and refunded transactions should not be counted as final successful revenue.

## SQL Validation

The KPI results were calculated first using Python. After that, SQL queries were used to validate the same metrics.

The SQL results matched the Python results, which confirms that the KPI calculations were correct.

## Dashboard Summary

A mini analytics KPI dashboard was created using Plotly.

The dashboard included:

- KPI metric cards
- Monthly revenue trend
- Order status distribution
- Payment status distribution

## Key Insights

The total successful revenue was AED 84,010.91 from 23 successful orders.

The successful order rate was low at 11.5%, meaning only a small part of all orders became completed and paid orders.

The average order value was AED 3,652.65, which shows that successful orders generate good revenue.

The returning customer rate was 15%, which means most successful customers only placed one successful order.

The payment success rate was 33.5%, while refunded and failed transactions were also high. This explains why the number of successful orders was low.

Monthly revenue was not stable. December 2025 and May 2026 had the highest revenue, while November 2025 and April 2026 had the lowest revenue.

## Conclusion

This task helped show how raw data can be transformed into useful business KPIs. Instead of only creating charts, the focus was on selecting important metrics, calculating them correctly, validating them with SQL, and presenting them in a dashboard.

Overall, the business has strong revenue per successful order, but the main issue is the low number of completed and paid orders.