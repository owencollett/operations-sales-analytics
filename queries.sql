-- Monthly revenue, profit, and profit margin
SELECT substr(order_date,1,7) AS month,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       ROUND(100.0*SUM(profit)/SUM(revenue),2) AS profit_margin_pct
FROM orders GROUP BY month ORDER BY month;

-- Regional operating performance
SELECT region, COUNT(*) AS orders,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       ROUND(AVG(delivery_days),2) AS avg_delivery_days,
       ROUND(100.0*AVG(late_delivery),2) AS late_delivery_rate_pct,
       ROUND(100.0*AVG(returned),2) AS return_rate_pct
FROM orders GROUP BY region ORDER BY revenue DESC;

-- Product category profitability
SELECT category, ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       ROUND(100.0*SUM(profit)/SUM(revenue),2) AS margin_pct
FROM orders GROUP BY category ORDER BY profit DESC;

-- Top five products by revenue within each category
WITH product_sales AS (
  SELECT category, product_id, SUM(revenue) AS product_revenue
  FROM orders GROUP BY category, product_id
), ranked AS (
  SELECT category, product_id, product_revenue,
         DENSE_RANK() OVER (PARTITION BY category ORDER BY product_revenue DESC) AS revenue_rank
  FROM product_sales
)
SELECT category, product_id, ROUND(product_revenue,2) AS product_revenue, revenue_rank
FROM ranked WHERE revenue_rank<=5 ORDER BY category, revenue_rank;

-- Return rate by delivery status
SELECT CASE WHEN late_delivery=1 THEN 'Late' ELSE 'On Time' END AS delivery_status,
       COUNT(*) AS orders, ROUND(100.0*AVG(returned),2) AS return_rate_pct
FROM orders GROUP BY delivery_status;
