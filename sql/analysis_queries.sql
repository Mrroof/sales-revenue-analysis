-- Run after loading sales_demo.csv into a SQL table named sales.
SELECT product, SUM(revenue) AS total_revenue,
       SUM(revenue - cost) AS gross_profit
FROM sales GROUP BY product ORDER BY total_revenue DESC;

SELECT region, SUM(revenue) AS total_revenue
FROM sales GROUP BY region ORDER BY total_revenue DESC;

SELECT order_month, SUM(revenue) AS monthly_revenue
FROM sales GROUP BY order_month ORDER BY order_month;
