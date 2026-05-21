-- ============================================================
-- Day 3: SQL Fundamentals Level 1
-- File: 01_select_basics.sql
-- Purpose: Practice basic SQL queries using SELECT, WHERE,
-- ORDER BY, LIMIT, DISTINCT, and basic filtering.
-- ============================================================


-- ============================================================
-- 1. Explore customers table
-- ============================================================

SELECT *
FROM customers
LIMIT 10;


-- ============================================================
-- 2. Show selected customer columns
-- ============================================================

SELECT customer_id, first_name, email, city, signup_date
FROM customers
LIMIT 10;


-- ============================================================
-- 3. Find the top 10 newest customers
-- ============================================================

SELECT customer_id, first_name, email, city, signup_date
FROM customers
ORDER BY signup_date DESC
LIMIT 10;


-- ============================================================
-- 4. Find the 10 oldest customers
-- ============================================================

SELECT customer_id, first_name, email, city, signup_date
FROM customers
ORDER BY signup_date ASC
LIMIT 10;


-- ============================================================
-- 5. Filter customers from Abu Dhabi
-- ============================================================

SELECT customer_id, first_name, email, city, signup_date
FROM customers
WHERE city = 'Abu Dhabi'
LIMIT 10;


-- ============================================================
-- 6. Filter customers by email domain
-- ============================================================

SELECT customer_id, first_name, email, city
FROM customers
WHERE email LIKE '%example.com'
LIMIT 10;


-- ============================================================
-- 7. Show unique customer cities
-- ============================================================

SELECT DISTINCT city
FROM customers
ORDER BY city;


-- ============================================================
-- 8. Explore products table
-- ============================================================

SELECT *
FROM products
LIMIT 10;


-- ============================================================
-- 9. List products ordered by price from highest to lowest
-- ============================================================

SELECT product_id, product_name, category, price
FROM products
ORDER BY price DESC
LIMIT 10;


-- ============================================================
-- 10. List products ordered by price from lowest to highest
-- ============================================================

SELECT product_id, product_name, category, price
FROM products
ORDER BY price ASC
LIMIT 10;


-- ============================================================
-- 11. Find products with price greater than 100
-- ============================================================

SELECT product_id, product_name, category, price
FROM products
WHERE price > 100
ORDER BY price DESC;


-- ============================================================
-- 12. Show unique product categories
-- ============================================================

SELECT DISTINCT category
FROM products
ORDER BY category;


-- ============================================================
-- 13. Explore orders table
-- ============================================================

SELECT *
FROM orders
LIMIT 10;


-- ============================================================
-- 14. Find newest orders
-- ============================================================

SELECT order_id, customer_id, order_date, status
FROM orders
ORDER BY order_date DESC
LIMIT 10;


-- ============================================================
-- 15. Find oldest orders
-- ============================================================

SELECT order_id, customer_id, order_date, status
FROM orders
ORDER BY order_date ASC
LIMIT 10;


-- ============================================================
-- 16. Find completed orders
-- ============================================================

SELECT order_id, customer_id, order_date, status
FROM orders
WHERE status = 'completed'
LIMIT 10;


-- ============================================================
-- 17. Show unique order statuses
-- ============================================================

SELECT DISTINCT status
FROM orders
ORDER BY status;


-- ============================================================
-- 18. Analyze daily orders
-- Since order_date is stored as text, we cast it to timestamp,
-- then convert it to date.
-- ============================================================

SELECT DATE(order_date::timestamp) AS order_day,
       COUNT(*) AS total_orders
FROM orders
GROUP BY DATE(order_date::timestamp)
ORDER BY order_day DESC
LIMIT 10;


-- ============================================================
-- 19. Analyze busiest order days
-- ============================================================

SELECT DATE(order_date::timestamp) AS order_day,
       COUNT(*) AS total_orders
FROM orders
GROUP BY DATE(order_date::timestamp)
ORDER BY total_orders DESC
LIMIT 10;


-- ============================================================
-- 20. Explore order_items table
-- ============================================================

SELECT *
FROM order_items
LIMIT 10;


-- ============================================================
-- 21. Find highest-value order items
-- ============================================================

SELECT order_item_id, order_id, product_id, quantity, unit_price, total_price
FROM order_items
ORDER BY total_price DESC
LIMIT 10;


-- ============================================================
-- 22. Find order items with quantity greater than 3
-- ============================================================

SELECT order_item_id, order_id, product_id, quantity, unit_price, total_price
FROM order_items
WHERE quantity > 3
ORDER BY quantity DESC
LIMIT 10;


-- ============================================================
-- 23. Explore transactions table
-- ============================================================

SELECT *
FROM transactions
LIMIT 10;


-- ============================================================
-- 24. Show unique payment methods
-- ============================================================

SELECT DISTINCT payment_method
FROM transactions
ORDER BY payment_method;


-- ============================================================
-- 25. Show unique payment statuses
-- ============================================================

SELECT DISTINCT payment_status
FROM transactions
ORDER BY payment_status;


-- ============================================================
-- 26. Find paid transactions
-- ============================================================

SELECT transaction_id, order_id, payment_method, payment_status, transaction_date, amount
FROM transactions
WHERE payment_status = 'paid'
ORDER BY amount DESC
LIMIT 10;


-- ============================================================
-- 27. Find failed transactions
-- ============================================================

SELECT transaction_id, order_id, payment_method, payment_status, transaction_date, amount
FROM transactions
WHERE payment_status = 'failed'
ORDER BY transaction_date DESC
LIMIT 10;


-- ============================================================
-- 28. Find highest transaction amounts
-- ============================================================

SELECT transaction_id, order_id, payment_method, payment_status, transaction_date, amount
FROM transactions
ORDER BY amount DESC
LIMIT 10;


-- ============================================================
-- 29. Analyze daily transaction amount
-- Since transaction_date is stored as text, we cast it to timestamp,
-- then convert it to date.
-- ============================================================

SELECT DATE(transaction_date::timestamp) AS transaction_day,
       COUNT(*) AS total_transactions,
       SUM(amount) AS total_amount
FROM transactions
GROUP BY DATE(transaction_date::timestamp)
ORDER BY transaction_day DESC
LIMIT 10;


-- ============================================================
-- 30. Conceptual query plan example
-- EXPLAIN shows how PostgreSQL plans to run the query.
-- ============================================================

EXPLAIN
SELECT customer_id, first_name, email, city, signup_date
FROM customers
ORDER BY signup_date DESC
LIMIT 10;


-- ============================================================
-- 31. Count total customers
-- ============================================================

SELECT COUNT(*) AS total_customers
FROM customers;


-- ============================================================
-- 32. Count total products
-- ============================================================

SELECT COUNT(*) AS total_products
FROM products;


-- ============================================================
-- 33. Count total orders
-- ============================================================

SELECT COUNT(*) AS total_orders
FROM orders;


-- ============================================================
-- 34. Count total order items
-- ============================================================

SELECT COUNT(*) AS total_order_items
FROM order_items;


-- ============================================================
-- 35. Count total transactions
-- ============================================================

SELECT COUNT(*) AS total_transactions
FROM transactions;


-- ============================================================
-- 36. Count customers by city
-- ============================================================

SELECT city,
       COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-- ============================================================
-- 37. Count products by category
-- ============================================================

SELECT category,
       COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;

-- ============================================================
-- 38. Count orders by status
-- ============================================================

SELECT status,
       COUNT(*) AS total_orders
FROM orders
GROUP BY status
ORDER BY total_orders DESC;

-- ============================================================
-- 39. Count transactions by payment method
-- ============================================================

SELECT payment_method,
       COUNT(*) AS total_transactions
FROM transactions
GROUP BY payment_method
ORDER BY total_transactions DESC;

-- ============================================================
-- 40. Count transactions by payment status
-- ============================================================

SELECT payment_status,
       COUNT(*) AS total_transactions
FROM transactions
GROUP BY payment_status
ORDER BY total_transactions DESC;