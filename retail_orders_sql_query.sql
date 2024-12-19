use retail_orders;
select * from orders;
select * from profit;

# show command displays the data type for each column
show columns from orders;
show columns from profit;

#convert the date column from text to date data type
alter table orders modify order_date DATE;
update orders set order_date = str_to_date(order_date,'%m/%d/%Y');

ALTER TABLE orders
ADD PRIMARY KEY (order_id);
ALTER TABLE profit
ADD PRIMARY KEY (product_id);
ALTER TABLE profit
ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);


#1.Top 10 highest revenue generating products
SELECT product_id, sum(sale_price * quantity) as revenue
FROM profit
GROUP BY product_id
ORDER BY sum(sale_price * quantity) DESC limit 10;

#2.Top 5 cities with the highest profit margins
SELECT city,sum(profit) as total_profit
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY city
ORDER BY SUM(profit) DESC limit 5;

#3.Calculate the total discount given for each category
SELECT category
	,sum(discount) AS total_discount
FROM profit
GROUP BY category;

#4.Find the average sale price per product category  --- recheck
SELECT category
	,avg(sale_price) AS avg_sale_price
FROM profit
GROUP BY category;

#5.Find the region with the highest average sale price
SELECT orders.region,avg(sale_price) as avg_sale_price
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY orders.region
ORDER BY avg(sale_price) DESC limit 1;

#6.Find the total profit per category 
SELECT category 
	,sum(profit) AS total_profit
FROM profit
GROUP BY category ORDER BY sum(profit) DESC;

#7.Identify the top 3 segments with the highest quantity of orders
SELECT orders.segment,sum(quantity) as total_quantity
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY orders.segment
ORDER BY SUM(quantity) DESC limit 3;

#8.Determine the average discount percentage given per region
SELECT orders.region
	,avg(profit.discount_percent) as avg_discount_percent
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY orders.region;

#9.Find the product category with the highest total profit
SELECT category
	,product_id
	,sum(profit) AS total_profit
FROM profit
GROUP BY category
	,product_id
ORDER BY total_profit DESC limit 1;

#10.Calculate the total revenue generated per year
SELECT year(orders.order_date) AS year
	,sum(profit.sale_price * profit.quantity) AS revenue
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY year(orders.order_date);

use retail_orders;

#11.Categories with profit greater than 10000.
SELECT category
	,sub_category
	,sum(profit) AS total_profit
FROM profit
GROUP BY category
	,sub_category
HAVING sum(profit) > 10000;

#12.List down the months based on the total profit for year 2022
SELECT MONTH(order_date) AS month,SUM(profit) AS profit_2022 
    FROM orders join profit on profit.order_id = orders.order_id where year(order_date) = 2022 GROUP BY MONTH(order_date)
ORDER BY profit_2022 DESC;

#13.Top 10 Products that has negative profit margin
select product_id,category,sum(profit) as total_profit from profit group by product_id,category order by sum(profit) limit 10;

#14.Calculate Total quantity of orders done per day
select dayname(order_date) as day_of_week,sum(quantity) as total_quantity from orders 
join profit on orders.order_id = profit.order_id
group by dayname(order_date) order by sum(quantity) DESC;

#15.Rank the product category based on its total revenue
select category,sum(sale_price * quantity) as total_revenue,rank() over (order by sum(sale_price * quantity) desc) as category_rank from orders join 
profit on orders.order_id = profit.order_id group by category;

#16.Order segment based on its total revenue
select segment,sum(sale_price * quantity) as revenue from orders join profit on orders.order_id = profit.order_id 
group by segment order by sum(sale_price * quantity) desc;

#17.List products which are having loss
SELECT product_id
	,profit
FROM profit
WHERE profit < 0
ORDER BY profit;

#18.Categorize discounts based on its discount percent
select category,discount_percent, case when discount_percent = 5 then 'Good discount percent' 
when discount_percent between 2 and 4 then 'Moderate discount percent' else 'low discount percent' end 
AS discount_category from profit group by category,discount_percent;

#19.Top 3 highest selling products
SELECT STATE
	,product_id
	,sum(quantity)
FROM orders
JOIN profit ON orders.order_id = profit.order_id
GROUP BY STATE
	,product_id
ORDER BY sum(quantity) DESC limit 3;
#20.Top 3 shipping modes used to deliver products
SELECT ship_mode
	,count(ship_mode) AS count
FROM orders
GROUP BY ship_mode
ORDER BY count(ship_mode) DESC limit 3;

