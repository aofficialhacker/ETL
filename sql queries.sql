use python_project;
select * from shoes;

# top 10 expensive shoes

select * from shoes order by prices desc limit 10;

# average prices by brand

select brand,avg(prices) from shoes group by brand;

# total no. of shoes by brand

select brand,count(title) as total_shoes from shoes group by brand;

# minimum and maximum price of shoes by brand

select brand,min(prices) as minimum_price,max(prices) as maximum_price from shoes group by brand;

# total no. of shoes between price range of 1000-1500

select count(title) as total_shoes from shoes where prices >= 1000 and prices<=1500;

# top 3 expensive shoes of each brand

select title,brand,prices from (select dense_rank() over (partition by brand order by prices desc) as dr,title,brand,prices from shoes) as ab where ab.dr<=3;

 # top 3 cheap shoes of each brand
 
select title,brand,prices from (select dense_rank() over (partition by brand order by prices) as dr,title,brand,prices from shoes) as ab where ab.dr<=3







