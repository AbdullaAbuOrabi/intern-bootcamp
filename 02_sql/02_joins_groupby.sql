-- ============================================================
-- Day 4: SQL Intermediate Level 2
-- File: 02_joins_groupby.sql
-- Purpose: Practice JOINs, GROUP BY, HAVING, CTEs, subqueries,
-- and data summarization for reporting.
-- ============================================================


-- ============================================================
-- 1. INNER JOIN orders with customers
-- Purpose:
-- Show each order with the customer who made it.
-- INNER JOIN only shows rows where the customer_id exists
-- in both orders and customers.
-- ============================================================

SELECT orders.order_id,
       customers.first_name,
       customers.email,
       orders.order_date,
       orders.status
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id
ORDER BY orders.order_date DESC
LIMIT 10;


-- ============================================================
-- 2. LEFT JOIN customers with orders
-- Purpose:
-- Show all customers, even if some customers do not have orders.
-- LEFT JOIN keeps all rows from the left table.
-- ============================================================

SELECT customers.customer_id,
       customers.first_name,
       customers.email,
       orders.order_id,
       orders.status
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id
ORDER BY customers.customer_id
LIMIT 20;


-- ============================================================
-- 3. RIGHT JOIN customers with orders
-- Purpose:
-- Show all orders, even if customer information is missing.
-- RIGHT JOIN keeps all rows from the right table.
-- ============================================================

SELECT orders.order_id,
       orders.customer_id,
       customers.first_name,
       customers.email,
       orders.status
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id
ORDER BY orders.order_id
LIMIT 20;


-- ============================================================
-- 4. Join orders, order_items, and products
-- Purpose:
-- Show which products were included in each order.
-- This connects order information with product information.
-- ============================================================

SELECT orders.order_id,
       products.product_name,
       products.category,
       order_items.quantity,
       order_items.unit_price,
       order_items.total_price
FROM orders
INNER JOIN order_items
ON orders.order_id = order_items.order_id
INNER JOIN products
ON order_items.product_id = products.product_id
ORDER BY orders.order_id
LIMIT 20;


-- ============================================================
-- 5. Full customer order details
-- Purpose:
-- Show who bought what.
-- This joins customers, orders, order_items, and products.
-- ============================================================

SELECT customers.first_name,
       customers.email,
       orders.order_id,
       products.product_name,
       products.category,
       order_items.quantity,
       order_items.total_price
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
INNER JOIN products
ON order_items.product_id = products.product_id
ORDER BY orders.order_id
LIMIT 20;


-- ============================================================
-- 6. Total revenue
-- Purpose:
-- Calculate total revenue from all order items.
-- SUM adds all total_price values together.
-- ============================================================

SELECT SUM(order_items.total_price) AS total_revenue
FROM order_items;


-- ============================================================
-- 7. Revenue by product category
-- Purpose:
-- Calculate how much revenue each product category made.
-- GROUP BY groups products by category.
-- ============================================================

SELECT products.category,
       SUM(order_items.total_price) AS category_revenue
FROM order_items
INNER JOIN products
ON order_items.product_id = products.product_id
GROUP BY products.category
ORDER BY category_revenue DESC;


-- ============================================================
-- 8. Total spending by customer
-- Purpose:
-- Calculate how much each customer spent in total.
-- This joins customers, orders, and order_items.
-- ============================================================

SELECT customers.customer_id,
       customers.first_name,
       customers.email,
       SUM(order_items.total_price) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY customers.customer_id,
         customers.first_name,
         customers.email
ORDER BY total_spent DESC
LIMIT 10;


-- ============================================================
-- 9. Customers with total spending greater than 500
-- Purpose:
-- Use HAVING to filter grouped customer spending results.
-- HAVING is used after GROUP BY.
-- ============================================================

SELECT customers.customer_id,
       customers.first_name,
       customers.email,
       SUM(order_items.total_price) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY customers.customer_id,
         customers.first_name,
         customers.email
HAVING SUM(order_items.total_price) > 500
ORDER BY total_spent DESC;


-- ============================================================
-- 10. Number of orders per customer
-- Purpose:
-- Count how many orders each customer made.
-- COUNT counts the number of order rows.
-- ============================================================

SELECT customers.customer_id,
       customers.first_name,
       customers.email,
       COUNT(orders.order_id) AS total_orders
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id,
         customers.first_name,
         customers.email
ORDER BY total_orders DESC
LIMIT 10;


-- ============================================================
-- 11. CTE for top customers
-- Purpose:
-- Use a CTE to calculate customer spending first.
-- Then select the top customers from that temporary result.
-- ============================================================

WITH customer_spending AS (
    SELECT customers.customer_id,
           customers.first_name,
           customers.email,
           SUM(order_items.total_price) AS total_spent
    FROM customers
    INNER JOIN orders
    ON customers.customer_id = orders.customer_id
    INNER JOIN order_items
    ON orders.order_id = order_items.order_id
    GROUP BY customers.customer_id,
             customers.first_name,
             customers.email
)
SELECT customer_id,
       first_name,
       email,
       total_spent
FROM customer_spending
ORDER BY total_spent DESC
LIMIT 10;


-- ============================================================
-- 12. Average order value using a subquery
-- Purpose:
-- First calculate each order total.
-- Then calculate the average value of all orders.
-- ============================================================

SELECT AVG(order_total) AS average_order_value
FROM (
    SELECT order_items.order_id,
           SUM(order_items.total_price) AS order_total
    FROM order_items
    GROUP BY order_items.order_id
) AS order_totals;