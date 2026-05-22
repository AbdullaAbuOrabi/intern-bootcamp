# Day 5 — Database Design & Mini Analytics Challenge

## Objective

The goal of this task was to practice database design fundamentals and use SQL to answer simple business questions from the e-commerce dataset.

This task focused on:

- Database normalization
- Primary keys and foreign keys
- Table relationships
- Constraints
- Indexes
- SQL-based analytics insights

The main deliverable files are:

- `02_sql/schema.sql`
- `02_sql/sql_summary.md`

---

## Database Design Summary

For this task, I designed a normalized relational schema for the e-commerce dataset.

The clean schema contains the following tables:

- customers_clean
- products_clean
- orders_clean
- order_items_clean
- transactions_clean

These tables were created separately because each table has one clear purpose.

The customers table stores customer information.

The products table stores product information.

The orders table stores order-level information.

The order_items table stores the products inside each order.

The transactions table stores payment information.

This design avoids storing all information in one large repeated table.

---

## Normalization Explanation

Normalization means organizing database tables so that data is stored clearly, repeated less, and connected using IDs.

In this project, the data was separated into different tables instead of storing customer details, product details, order details, and payment details in one big table.

This helps make the database easier to maintain and reduces repeated data.

For example, customer information is stored once in the customers table, and product information is stored once in the products table.

Orders and order items connect to those tables using IDs.

---

## Keys and Relationships

Primary keys were used to uniquely identify each row in a table.

Examples:

- customers_clean.customer_id
- products_clean.product_id
- orders_clean.order_id
- order_items_clean.order_item_id
- transactions_clean.transaction_id

Foreign keys were used to connect related tables.

Relationships used:

- orders_clean.customer_id references customers_clean.customer_id
- order_items_clean.order_id references orders_clean.order_id
- order_items_clean.product_id references products_clean.product_id
- transactions_clean.order_id references orders_clean.order_id

These relationships show how the e-commerce data connects together.

A customer can have many orders.

An order can have many order items.

Each order item belongs to one product.

Each transaction belongs to one order.

---

## Constraints Used

Constraints were added to protect the data and prevent invalid values.

Examples:

- PRIMARY KEY was used to uniquely identify rows.
- FOREIGN KEY was used to protect table relationships.
- NOT NULL was used for required fields.
- UNIQUE was used for customer email.
- CHECK was used to prevent invalid numeric values.

Examples from the schema:

- Product price cannot be negative.
- Quantity must be greater than zero.
- Unit price cannot be negative.
- Total price cannot be negative.
- Transaction amount cannot be negative.

These rules help keep the database clean and reliable.

---

## Indexes Created

Indexes were created on columns commonly used in joins, filtering, and reporting.

Indexes created:

- idx_orders_clean_customer_id
- idx_orders_clean_order_date
- idx_order_items_clean_order_id
- idx_order_items_clean_product_id
- idx_transactions_clean_order_id
- idx_transactions_clean_payment_status

Indexes help PostgreSQL find rows faster.

For example, orders_clean.customer_id was indexed because it is commonly used to connect orders with customers.

order_items_clean.order_id was indexed because it is commonly used to connect order items with orders.

order_date was indexed because it can be used for sales period analysis.

An index does not create a table relationship. The foreign key creates the relationship. The index helps PostgreSQL search and join faster.

---

## Analytics Challenge

After creating the schema, I wrote SQL queries to answer business-style questions using the existing loaded tables.

The clean tables were created to demonstrate database design. The analytics queries were run on the original loaded tables because they contain the ingested CSV data.

---

## Query 1 — Identify Peak Sales Periods

Business question:

Which days had the highest sales revenue?

Query excerpt:

```sql
SELECT DATE(orders.order_date::timestamp) AS sales_day,
       SUM(order_items.total_price) AS daily_revenue
FROM orders
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY DATE(orders.order_date::timestamp)
ORDER BY daily_revenue DESC
LIMIT 10;