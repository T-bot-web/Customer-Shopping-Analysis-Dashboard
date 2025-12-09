-- Total sales
SELECT SUM(purchase_amount_usd) AS total_sales FROM customers;

-- Sales by category
SELECT category, SUM(purchase_amount_usd) AS total_sales
FROM customers
GROUP BY category
ORDER BY total_sales DESC;

-- Sales by season
SELECT season, SUM(purchase_amount_usd) AS total_sales
FROM customers
GROUP BY season
ORDER BY total_sales DESC;

-- KPI counts
SELECT COUNT(DISTINCT customer_id) AS total_customers, COUNT(*) AS total_transactions,
       AVG(review_rating) AS avg_rating
FROM customers;

-- Payment method distribution
SELECT payment_method, COUNT(*) AS count_customers
FROM customers
GROUP BY payment_method
ORDER BY count_customers DESC;
