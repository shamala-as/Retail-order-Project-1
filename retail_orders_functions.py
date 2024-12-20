import streamlit as st
import pandas as pd
import mysql.connector

#Questions
qn_one = '1.Top 10 highest revenue generating products'
qn_two = '2.Top 5 cities with the highest profit margins'
qn_three = '3.Total discount given for each category'
qn_four = '4.Average sale price per product category'
qn_five = '5.Region with the highest average sale price'
qn_six = '6.Total profit per category'
qn_seven = '7.Top 3 segments with the highest quantity of orders'
qn_eight = '8.Average discount percentage given per region'
qn_nine = '9.Product category with the highest total profit'
qn_ten = '10.Total revenue generated per year'
qn_eleven = '11.Categories with profit greater than 10000'
qn_twelve = '12.List down the months based on the total profit for year 2022'
qn_thirteen = '13.Top 10 Products that has negative profit margin'
qn_fourteen = '14.Calculate Total quantity of orders done per day'
qn_fifteen = '15.Rank the product category based on its total revenue'
qn_sixteen = '16.Order segment based on its total revenue'
qn_seventeen = '17.List products which are having loss'
qn_eighteen = '18.Categorize discounts based on its discount percent'
qn_nineteen = '19.Top 3 highest selling products'
qn_twenty = '20.Top 3 shipping modes used to deliver products'

#Generating the query for the selected question

def generate_query(question):
        questionMap = {
        qn_one :'SELECT product_id, sum(sale_price * quantity) as revenue FROM profit GROUP BY product_id ORDER BY sum(sale_price * quantity) DESC limit 10',
        qn_two : 'SELECT city,sum(profit) as total_profit FROM orders JOIN profit ON orders.order_id = profit.order_id GROUP BY city ORDER BY SUM(profit) DESC limit 5',
        qn_three : 'SELECT category,sum(discount) AS total_discount FROM profit GROUP BY category',
        qn_four : 'SELECT category,avg(sale_price) AS avg_sale_price FROM profit GROUP BY category',
        qn_five : 'SELECT orders.region,avg(sale_price) as avg_sale_price FROM orders JOIN profit ON orders.order_id = profit.order_id GROUP BY orders.region ORDER BY avg(sale_price) DESC limit 1',
        qn_six : 'SELECT category,sum(profit) AS total_profit FROM profit GROUP BY category ORDER BY sum(profit) DESC',
        qn_seven : 'SELECT orders.segment,sum(quantity) as total_quantity FROM orders JOIN profit ON orders.order_id = profit.order_id GROUP BY orders.segment ORDER BY SUM(quantity) DESC limit 3',
        qn_eight : 'SELECT orders.region,avg(profit.discount_percent) as avg_discount_percent FROM orders JOIN profit ON orders.order_id = profit.order_id GROUP BY orders.region',
        qn_nine : 'SELECT category,product_id,sum(profit) AS total_profit FROM profit GROUP BY category,product_id ORDER BY total_profit DESC limit 1',
        qn_ten : 'SELECT year(orders.order_date) as year, sum(profit.sale_price * profit.quantity) as revenue from orders join profit on orders.order_id = profit.order_id group by year(orders.order_date)',
        qn_eleven : 'SELECT category,sub_category,sum(profit) as total_profit from profit group by category,sub_category having sum(profit) > 10000',
        qn_twelve : 'SELECT MONTH(order_date) AS month,SUM(profit) AS profit_2022 FROM orders join profit on profit.order_id = orders.order_id where year(order_date) = 2022 GROUP BY MONTH(order_date) ORDER BY profit_2022 DESC',
        qn_thirteen : 'SELECT product_id,category,sum(profit) AS total_profit from profit group by product_id,category order by sum(profit) limit 10',
        qn_fourteen : 'SELECT dayname(order_date) AS day_of_week,sum(quantity) as total_quantity from orders join profit on orders.order_id = profit.order_id group by dayname(order_date) order by sum(quantity) DESC',
        qn_fifteen : 'SELECT category,sum(sale_price * quantity) AS total_revenue,rank() over (order by sum(sale_price * quantity) DESC) AS category_rank from orders join profit on orders.order_id = profit.order_id group by category',
        qn_sixteen : 'SELECT segment,sum(sale_price * quantity) AS revenue from orders join profit on orders.order_id = profit.order_id group by segment order by sum(sale_price * quantity) DESC',
        qn_seventeen : 'SELECT product_id,profit from profit where profit < 0 order by profit',
        qn_eighteen :  """ 
        select category,discount_percent, case when discount_percent = 5 then 'Good discount percent' 
        when discount_percent between 2 and 4 then 'Moderate discount percent' else 'low discount percent' end 
        AS discount_category from profit group by category,discount_percent
        """,
        qn_nineteen : 'SELECT state,product_id,sum(quantity) from orders join profit on orders.order_id = profit.order_id group by state,product_id order by sum(quantity) DESC limit 3',
        qn_twenty : 'select ship_mode,count(ship_mode) as count from orders group by ship_mode order by count(ship_mode) desc limit 3'
        }
        return questionMap.get(question)