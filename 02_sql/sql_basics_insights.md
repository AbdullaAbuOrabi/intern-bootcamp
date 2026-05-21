# Day 3 — SQL Fundamentals Level 1

## Objective

The goal of this task was to practice basic SQL queries using the PostgreSQL tables that were loaded during the CSV ingestion task.

The main focus was on using:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT

The queries were written and stored in:

`02_sql/01_select_basics.sql`

---

## Tables Explored

The following tables were explored:

- customers
- products
- orders
- order_items
- transactions

These tables were already loaded into PostgreSQL during the previous data ingestion task.

---

## Table Columns

### customers

The customers table contains:

- customer_id
- first_name
- email
- city
- signup_date

This table stores customer information such as the customer name, email, city, and signup date.

---

### products

The products table contains:

- product_id
- product_name
- category
- price

This table stores product information such as product name, category, and price.

---

### orders

The orders table contains:

- order_id
- customer_id
- order_date
- status

This table stores order information such as which customer made the order, the order date, and the order status.

---

### order_items

The order_items table contains:

- order_item_id
- order_id
- product_id
- quantity
- unit_price
- total_price

This table stores the products inside each order, including quantity, unit price, and total price.

---

### transactions

The transactions table contains:

- transaction_id
- order_id
- payment_method
- payment_status
- transaction_date
- amount

This table stores payment information for orders, including payment method, payment status, transaction date, and amount.

---

## Key SQL Concepts Practiced

### SELECT

SELECT was used to choose which columns to display from a table.

Example:

`SELECT customer_id, first_name, email FROM customers;`

This helped me view only the columns I needed instead of showing the full table.

---

### WHERE

WHERE was used to filter rows based on a condition.

Example:

`WHERE city = 'Abu Dhabi'`

This helped me find only customers from Abu Dhabi.

Another example:

`WHERE price > 100`

This helped me find only products with a price greater than 100.

---

### ORDER BY

ORDER BY was used to sort query results.

Example:

`ORDER BY signup_date DESC`

This helped me sort customers from newest to oldest.

DESC means descending order.

Examples:

- newest to oldest
- highest to lowest

ASC means ascending order.

Examples:

- oldest to newest
- lowest to highest

---

### LIMIT

LIMIT was used to control how many rows are displayed.

Example:

`LIMIT 10`

This helped me show only the first 10 rows instead of displaying the full table.

---

### DISTINCT

DISTINCT was used to show unique values only.

Example:

`SELECT DISTINCT city FROM customers;`

This helped me identify the available customer cities without showing duplicate values.

Another example:

`SELECT DISTINCT category FROM products;`

This helped me identify the available product categories.

---

## Outputs and Insights

### Top 10 Newest Customers

I used `ORDER BY signup_date DESC` with `LIMIT 10` to show the newest customers.

Insight:

This query helps identify the most recently registered customers in the system.

---

### Oldest Customers

I used `ORDER BY signup_date ASC` to show the oldest customers.

Insight:

This query helps identify the earliest customers who signed up.

---

### Customers by City

I used a WHERE condition to filter customers from a specific city.

Example:

`WHERE city = 'Abu Dhabi'`

Insight:

This query helps analyze customers based on location.

---

### Unique Customer Cities

I used DISTINCT to list the unique customer cities.

Insight:

This helps understand where customers are located in the dataset.

---

### Product Price Analysis

I sorted products by price from highest to lowest and from lowest to highest.

Insight:

This helps identify the most expensive and cheapest products in the product catalog.

---

### Products Above 100

I used a WHERE condition to filter products with a price greater than 100.

Insight:

This query helps focus on higher-priced products.

---

### Unique Product Categories

I used DISTINCT to list product categories.

Insight:

This helps understand what types of products exist in the dataset.

---

### Newest Orders

I sorted the orders table by order_date.

Insight:

This helps identify the most recent customer orders.

---

### Completed Orders

I filtered the orders table by status.

Example:

`WHERE status = 'completed'`

Insight:

This helps focus only on orders that were completed successfully.

---

### Unique Order Statuses

I used DISTINCT to show all available order statuses.

Insight:

This helps understand the different order states in the system.

---

### Daily Orders

I grouped orders by date and counted how many orders happened per day.

Insight:

This helps understand order activity over time and identify busy days.

---

### Order Items Analysis

I explored the order_items table and sorted by total_price.

Insight:

This helps identify the highest-value items inside orders.

I also filtered order items where quantity was greater than 3.

Insight:

This helps identify orders that contain larger quantities of products.

---

### Payment Method Analysis

I used DISTINCT to show unique payment methods.

Insight:

This helps understand how customers are paying, such as card or cash.

---

### Payment Status Analysis

I used DISTINCT to show unique payment statuses.

Insight:

This helps identify possible payment states such as paid or failed.

---

### Paid Transactions

I filtered transactions where payment_status was paid.

Insight:

This helps focus on successful payments.

---

### Failed Transactions

I filtered transactions where payment_status was failed.

Insight:

This helps identify unsuccessful payments that may need review.

---

### Highest Transaction Amounts

I sorted transactions by amount from highest to lowest.

Insight:

This helps identify the largest payments in the system.

---

### Daily Transaction Amount

I grouped transactions by transaction date and calculated the total amount per day.

Insight:

This helps understand payment activity over time.

---

## Query Plan Concept

I used EXPLAIN on one query to understand how PostgreSQL plans to execute it.

Example:

`EXPLAIN SELECT customer_id, first_name, email, city, signup_date FROM customers ORDER BY signup_date DESC LIMIT 10;`

At this stage, I learned that EXPLAIN does not show the final data output. Instead, it shows the execution plan that PostgreSQL uses internally.

This is useful later when working with larger datasets and trying to understand query performance.

---

## Important Note About Date Columns

In this dataset, date columns such as order_date and transaction_date are stored as text.

Because of that, when I wanted to group by date, I used casting:

`order_date::timestamp`

and:

`transaction_date::timestamp`

This converts the text value into a timestamp so PostgreSQL can treat it like a real date/time value.

---

## Summary

In this task, I practiced writing basic SQL queries to explore and analyze data from PostgreSQL.

I learned how to select columns, filter rows, sort results, limit outputs, find unique values, and understand query execution conceptually.

This task helped me move from loading data into the database to analyzing and understanding the data using SQL.