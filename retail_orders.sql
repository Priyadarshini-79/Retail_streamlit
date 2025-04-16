-- 1 Top 10 highest revenue-generating products
SELECT product_id,SUM(Revenue) AS total_revenue
FROM orders
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;

-- 2 Top 5 cities with the highest profit margins
SELECT City,SUM(Profit) AS total_profit
FROM orders
GROUP BY City
ORDER BY total_profit DESC
LIMIT 5;

-- 3 Total discount for each category
SELECT category,SUM(discount_percent) AS total_discount
FROM orders
GROUP BY category;

-- 4 Average sale price per product category
SELECT category,AVG(sale_price) AS average_sale_price
FROM orders
GROUP BY category;

-- 5 Region with the highest average sale price
SELECT Region, avg(sale_price) AS avg_sale_price
FROM orders
GROUP BY Region
ORDER BY avg_sale_price DESC
LIMIT 1;

-- 6 Total Profit Per Category
SELECT category,SUM(Profit) AS total_profit
FROM orders
GROUP BY category;

-- 7 Top 3 segments with the highest quantity of orders
SELECT Segment,SUM(Quantity) AS total_orders
FROM orders
GROUP BY Segment
ORDER BY total_orders DESC
LIMIT 3;

-- 8 The Average Discount Percentage Given Per Region
SELECT Region,AVG(discount_percent) AS avg_discount_percentage
FROM orders
GROUP BY Region;

-- 9 The product category with the highest total profit
SELECT category,SUM(Profit) AS total_profit
FROM orders
GROUP BY category
ORDER BY total_profit DESC
LIMIT 1;

-- 10 Total Revenue Generated Per Year
SELECT YEAR(order_date) AS year,SUM(Revenue) AS total_revenue
FROM orders
GROUP BY YEAR(order_date)
ORDER BY year;

-- 11 Top 5 Products with the Highest Total Profit
SELECT product_id,SUM(Profit) AS total_profit
FROM orders
GROUP BY product_id
ORDER BY total_profit DESC
LIMIT 5;

-- 12 Product Category with the Highest Discount Percentage
SELECT category,AVG(discount_percent) AS avg_discount
FROM orders
GROUP BY category
ORDER BY avg_discount DESC
LIMIT 1;

-- 13 Total Sales for Each Month and Year
SELECT YEAR(order_date) AS year,MONTH(order_date) AS month,SUM(Revenue) AS total_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- 14 Total Number of Orders by Region
SELECT Region,COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY Region;

-- 15 Product with the Highest Profit Margin
SELECT product_id,AVG(Profit_Margin) AS avg_profit_margin
FROM orders
GROUP BY product_id
ORDER BY avg_profit_margin DESC
LIMIT 1;

-- 16 Average Order Value by Region
SELECT Region,AVG(Revenue) AS avg_order_value
FROM orders
GROUP BY Region;

-- 17 Total Revenue Per Product Category by Year
SELECT category,YEAR(order_date) AS year,SUM(Revenue) AS total_revenue
FROM orders
GROUP BY category, YEAR(order_date)
ORDER BY category, year;

-- 18 Most Profitable Product in Each Category
WITH ranked_products AS (
    SELECT 
        category,
        product_id,
        SUM(Profit) AS total_profit,
        ROW_NUMBER() OVER(PARTITION BY category ORDER BY SUM(Profit) DESC) AS ranking
    FROM orders
    GROUP BY category, product_id
)
SELECT category,product_id,total_profit
FROM ranked_products
WHERE ranking = 1;

-- 19 Profit-to-Revenue Ratio for Each Category
SELECT category,(SUM(Profit) / SUM(Revenue)) * 100 AS profit_to_revenue_ratio
FROM orders
GROUP BY category;

-- 20 Percentage Contribution of Each Product Category to Total Sales
WITH category_sales AS (
    SELECT category,SUM(Revenue) AS total_sales
    FROM orders
    GROUP BY category
)
SELECT category,(total_sales / (SELECT SUM(Revenue) FROM orders)) * 100 AS contribution_percentage
FROM category_sales
ORDER BY contribution_percentage DESC;

















