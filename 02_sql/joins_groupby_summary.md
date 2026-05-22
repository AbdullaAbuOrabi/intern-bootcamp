# Day 4 — SQL Intermediate Level 2

## Objective

The goal of this task was to practice intermediate SQL concepts using the PostgreSQL tables that were loaded during the data ingestion task.

The main focus was on:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- GROUP BY
- HAVING
- SUM
- AVG
- COUNT
- CTEs
- Subqueries
- Data summarization for reporting

The queries were written and stored in:

`02_sql/02_joins_groupby.sql`

---

## Tables Used

The following tables were used:

- customers
- orders
- order_items
- products

These tables are related using shared columns:

- customers.customer_id connects to orders.customer_id
- orders.order_id connects to order_items.order_id
- order_items.product_id connects to products.product_id

These relationships allowed me to connect customer information, order information, and product information together.

---

## Key SQL Concepts Practiced

### INNER JOIN

INNER JOIN was used to return only rows where there is a match in both joined tables.

Example:

`orders.customer_id = customers.customer_id`

This means the orders table and customers table are connected using customer_id.

Insight:

INNER JOIN helped me show each order with the customer who made that order.

---

### LEFT JOIN

LEFT JOIN was used to keep all rows from the left table, even if there is no matching row in the right table.

Example:

`customers LEFT JOIN orders`

This means all customers are shown, even if some customers do not have orders.

Insight:

LEFT JOIN is useful when I want to keep the full list of customers and check whether each customer has an order or not.

---

### RIGHT JOIN

RIGHT JOIN was used to keep all rows from the right table, even if there is no matching row in the left table.

Example:

`customers RIGHT JOIN orders`

This means all orders are shown, even if customer information is missing.

Insight:

RIGHT JOIN is useful when the main focus is the right table. In this case, it helps make sure all orders appear in the result.

---

### GROUP BY

GROUP BY was used to group rows that have the same value so I could summarize them.

Examples:

- Grouping by product category
- Grouping by customer
- Grouping by order_id

Insight:

GROUP BY helped turn detailed rows into summary reports, such as revenue by category, spending by customer, and total value per order.

---

### HAVING

HAVING was used to filter grouped results after aggregation.

Example:

`HAVING SUM(order_items.total_price) > 500`

This means the query first calculates total spending for each customer, then only shows customers whose total spending is greater than 500.

Insight:

HAVING is different from WHERE. WHERE filters normal rows before grouping, while HAVING filters grouped results after calculations like SUM or COUNT.

---

### SUM

SUM was used to add numeric values together.

Examples:

- `SUM(order_items.total_price)`
- `SUM(order_items.quantity)`

Insight:

SUM helped calculate total revenue, category revenue, customer spending, and order totals.

---

### AVG

AVG was used to calculate the average value.

Example:

`AVG(order_total)`

Insight:

AVG helped calculate the average order value after each order total was calculated first.

---

### COUNT

COUNT was used to count rows.

Example:

`COUNT(orders.order_id)`

Insight:

COUNT helped calculate how many orders each customer made.

---

### CTE

CTE stands for Common Table Expression.

A CTE creates a temporary named result that can be used in the main query.

Example:

`WITH customer_spending AS (...)`

Insight:

The CTE made the top customers query easier to read because the customer spending calculation was separated from the final selection.

---

### Subquery

A subquery is a query inside another query.

In this task, a subquery was used to calculate order totals first, then calculate the average order value.

Insight:

Subqueries are useful when one calculation depends on another calculation.

---

## Outputs and Insights

### Orders with Customer Details

I joined the orders table with the customers table using customer_id.

Insight:

This query showed which customer made each order. It connected order information such as order_id, order_date, and status with customer information such as first_name and email.

---

### Customers with Orders Using LEFT JOIN

I used LEFT JOIN from customers to orders.

Insight:

This query kept all customers in the output, even if a customer did not have an order. This is useful when checking customer activity.

---

### Orders with Customer Details Using RIGHT JOIN

I used RIGHT JOIN between customers and orders.

Insight:

This query kept all orders in the output, even if customer information was missing. This is useful when the order table is the main focus.

---

### Orders with Product Details

I joined orders, order_items, and products.

Insight:

This query showed which products were included in each order. It connected order details with product names, categories, quantities, unit prices, and total prices.

---

### Full Customer Order Details

I joined customers, orders, order_items, and products.

Insight:

This query gave a full view of who bought what. It connected customer information, order information, and product information in one result.

---

### Total Revenue

I used SUM(total_price) from the order_items table.

Insight:

This query calculated the total revenue from all order items. It helped summarize the total sales value in the dataset.

---

### Revenue by Product Category

I joined order_items with products and grouped the results by product category.

Insight:

This query showed how much revenue each product category generated. It is useful for understanding which categories performed better in sales.

---

### Total Spending by Customer

I joined customers, orders, and order_items, then grouped the result by customer.

Insight:

This query showed how much each customer spent in total. It helped identify the highest-spending customers.

---

### Customers with Spending Greater Than 500

I used HAVING with SUM(total_price) to filter customers whose total spending was greater than 500.

Insight:

This query helped identify high-value customers based on total spending.

---

### Number of Orders Per Customer

I joined customers with orders and counted the number of orders per customer.

Insight:

This query helped identify how many orders each customer made.

---

### Top Customers Using CTE

I used a CTE called customer_spending to calculate total spending by customer first, then selected the top customers from that result.

Insight:

The CTE made the query easier to understand because the customer spending calculation was separated from the final selection.

---

### Average Order Value Using a Subquery

I used a subquery to calculate the total value of each order first, then used AVG to calculate the average order value.

Insight:

This helped understand the average amount spent per order.

---

## Important Difference Between WHERE and HAVING

WHERE filters rows before grouping.

Example:

`WHERE orders.status = 'completed'`

This filters the order rows first and keeps only completed orders.

HAVING filters grouped results after aggregation.

Example:

`HAVING SUM(order_items.total_price) > 500`

This calculates total spending for each customer first, then keeps only customers whose total spending is greater than 500.

Simple explanation:

- WHERE filters normal rows.
- HAVING filters summarized results.

---

## Important Difference Between JOIN Types

INNER JOIN returns only matching rows from both tables.

LEFT JOIN returns all rows from the left table and matching rows from the right table.

RIGHT JOIN returns all rows from the right table and matching rows from the left table.

In this task:

- INNER JOIN was useful when I wanted only connected records.
- LEFT JOIN was useful when I wanted to keep all customers.
- RIGHT JOIN was useful when I wanted to keep all orders.

---

## Summary

In this task, I practiced intermediate SQL queries by connecting multiple tables together.

I learned how JOINs are used to combine related tables, how GROUP BY is used to summarize data, and how HAVING is used to filter summarized results.

I also practiced SUM, AVG, COUNT, CTEs, and subqueries.

This task helped me move from basic single-table SQL queries to multi-table analysis and reporting.

The main outcome of this task was understanding how relational tables work together and how SQL can be used to create reports such as total revenue, revenue by category, total spending by customer, high-value customers, order counts, top customers, and average order value.