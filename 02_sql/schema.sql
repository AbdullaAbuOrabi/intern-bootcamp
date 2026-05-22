-- ============================================================
-- Day 5: Database Design & Mini Analytics Challenge
-- File: schema.sql
-- Purpose: Design a normalized relational schema for the
-- e-commerce dataset using keys, relationships, constraints,
-- and indexes.
-- ============================================================


-- ============================================================
-- 1. Drop tables if they already exist
-- Purpose:
-- This makes the script reusable while developing.
-- Tables are dropped in reverse relationship order because
-- child tables depend on parent tables.
-- ============================================================

DROP TABLE IF EXISTS transactions_clean;
DROP TABLE IF EXISTS order_items_clean;
DROP TABLE IF EXISTS orders_clean;
DROP TABLE IF EXISTS products_clean;
DROP TABLE IF EXISTS customers_clean;


-- ============================================================
-- 2. Create customers table
-- Purpose:
-- Store customer details.
-- customer_id is the primary key because it uniquely identifies
-- each customer.
-- ============================================================

CREATE TABLE customers_clean (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    city TEXT,
    signup_date TIMESTAMP
);


-- ============================================================
-- 3. Create products table
-- Purpose:
-- Store product details.
-- product_id is the primary key because it uniquely identifies
-- each product.
-- price must not be negative.
-- ============================================================

CREATE TABLE products_clean (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);


-- ============================================================
-- 4. Create orders table
-- Purpose:
-- Store order-level information.
-- Each order belongs to one customer.
-- customer_id is a foreign key that connects orders to customers.
-- ============================================================

CREATE TABLE orders_clean (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP,
    status TEXT NOT NULL,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers_clean(customer_id)
);


-- ============================================================
-- 5. Create order_items table
-- Purpose:
-- Store item-level details for each order.
-- Each row represents one product inside an order.
-- order_id connects to orders.
-- product_id connects to products.
-- quantity and prices must not be negative.
-- ============================================================

CREATE TABLE order_items_clean (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0),
    total_price NUMERIC(10, 2) NOT NULL CHECK (total_price >= 0),
    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders_clean(order_id),
    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES products_clean(product_id)
);


-- ============================================================
-- 6. Create transactions table
-- Purpose:
-- Store payment details for each order.
-- order_id connects transactions to orders.
-- amount must not be negative.
-- ============================================================

CREATE TABLE transactions_clean (
    transaction_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    payment_method TEXT NOT NULL,
    payment_status TEXT NOT NULL,
    transaction_date TIMESTAMP,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
    CONSTRAINT fk_transactions_order
        FOREIGN KEY (order_id)
        REFERENCES orders_clean(order_id)
);


-- ============================================================
-- 7. Create indexes
-- Purpose:
-- Indexes help PostgreSQL find and join data faster.
-- These indexes are created on columns commonly used for joins,
-- filtering, and reporting.
-- ============================================================

CREATE INDEX idx_orders_clean_customer_id
ON orders_clean(customer_id);

CREATE INDEX idx_orders_clean_order_date
ON orders_clean(order_date);

CREATE INDEX idx_order_items_clean_order_id
ON order_items_clean(order_id);

CREATE INDEX idx_order_items_clean_product_id
ON order_items_clean(product_id);

CREATE INDEX idx_transactions_clean_order_id
ON transactions_clean(order_id);

CREATE INDEX idx_transactions_clean_payment_status
ON transactions_clean(payment_status);


-- ============================================================
-- 8. Example EXPLAIN query
-- Purpose:
-- EXPLAIN shows how PostgreSQL plans to run a query.
-- This can be used before and after indexes to understand
-- performance conceptually.
-- ============================================================

EXPLAIN
SELECT orders_clean.order_id,
       customers_clean.first_name,
       orders_clean.order_date
FROM orders_clean
INNER JOIN customers_clean
ON orders_clean.customer_id = customers_clean.customer_id
WHERE orders_clean.order_date IS NOT NULL;

-- ============================================================
-- 9. Analytics Challenge: Identify peak sales periods
-- Business question:
-- Which days had the highest sales revenue?
-- ============================================================

SELECT DATE(orders.order_date::timestamp) AS sales_day,
       SUM(order_items.total_price) AS daily_revenue
FROM orders
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY DATE(orders.order_date::timestamp)
ORDER BY daily_revenue DESC
LIMIT 10;


-- ============================================================
-- 10. Analytics Challenge: Customer segments by city
-- Business question:
-- Which customer cities contributed the most revenue?
-- ============================================================

SELECT customers.city,
       SUM(order_items.total_price) AS total_revenue
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY customers.city
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- 11. Analytics Challenge: Revenue by order status
-- Business question:
-- Which order statuses are connected to the highest total revenue?
-- ============================================================

SELECT orders.status,
       COUNT(DISTINCT orders.order_id) AS total_orders,
       SUM(order_items.total_price) AS total_revenue
FROM orders
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY orders.status
ORDER BY total_revenue DESC;