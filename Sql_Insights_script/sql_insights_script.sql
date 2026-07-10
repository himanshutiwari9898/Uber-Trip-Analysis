create database uber;
use uber;
show tables;
select * from customers
limit 10;

select * from drivers
limit 10;

select * from trips
limit 10;



select @@sql_safe_updates;
set sql_safe_updates = 0;

alter table trips
add booking_date DATE,
add booking_time TIME;

alter table trips
drop column booking_datetime;

update trips
set booking_date = DATE(booking_datetime),
    booking_time = TIME(booking_datetime);



-- 1. Daily Revenue Summary
CREATE TABLE daily_revenue_summary AS
SELECT
DATE(booking_date) AS trip_date,
COUNT(*) AS total_trips,
SUM(fare) AS total_revenue,
AVG(fare) AS avg_fare
FROM trips
WHERE trip_status='Completed'
GROUP BY DATE(booking_date)
ORDER BY trip_date;
select * from daily_revenue_summary;


-- 2. Vehical Performance
CREATE TABLE vehicle_summary AS
SELECT
vehicle_type,
COUNT(*) AS total_trips,
SUM(fare) AS revenue,
AVG(fare) AS avg_fare,
AVG(distance_km) avg_distance
FROM trips
WHERE trip_status='Completed'
GROUP BY vehicle_type;
select * from vehicle_summary;

-- 3. top pickup location
CREATE TABLE pickup_summary AS
SELECT
pickup_location,
COUNT(*) total_pickups,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY pickup_location
ORDER BY total_pickups DESC;

rename table pickup_summary to top_pickup_locations;
select * from top_pickup_locations;

-- 4. top drop loactions
CREATE TABLE top_drop_locations AS

SELECT
drop_location,
COUNT(*) total_dropoffs,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY drop_location
ORDER BY total_dropoffs DESC;

select * from top_drop_locations;

-- 5. Driver Performance
CREATE TABLE driver_performance AS
SELECT
d.driver_id,
d.driver_name,
d.vehicle_type,
COUNT(t.trip_id) total_trips,
SUM(t.fare) revenue,
ROUND(AVG(t.driver_rating),2) avg_rating
FROM drivers d
JOIN trips t
ON d.driver_id=t.driver_id
WHERE t.trip_status='Completed'
GROUP BY d.driver_id,d.driver_name,d.vehicle_type;

select * from driver_performance;

-- 6. CustomerSummary
CREATE TABLE customer_summary AS
SELECT
c.customer_id,
c.customer_name,
COUNT(t.trip_id) total_trips,
SUM(t.fare) total_spent,
ROUND(AVG(t.customer_rating),2) avg_rating
FROM customers c
JOIN trips t
ON c.customer_id=t.customer_id
WHERE t.trip_status='Completed'
GROUP BY c.customer_id,c.customer_name;

select * from customer_summary;

-- 7. Cancelattion Analysis
CREATE TABLE cancellation_summary AS
SELECT
trip_status,
cancellation_reason,
COUNT(*) total
FROM trips
GROUP BY trip_status,cancellation_reason;

select * from cancellation_summary;

-- 8.Payment Method Analysis
CREATE TABLE payment_method AS
SELECT
payment_method,
COUNT(*) total_transactions,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY payment_method;

select*from payment_method;

-- 9.Hourly Demand
CREATE TABLE hourly_demand AS
SELECT DATE_FORMAT(booking_time, '%l %p') as booking_hour,
COUNT(*) total_trips,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY booking_hour
ORDER BY booking_hour;

select * from hourly_demand;

-- 10. Monthly Revenue

CREATE TABLE monthly_revenue AS
SELECT
MONTH(booking_date) month,
MONTHNAME(booking_date) month_name,
COUNT(*) trips,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY month,month_name
ORDER BY month;

select * from monthly_revenue;

-- 11. City wise Performance

CREATE TABLE city_performance AS
SELECT
c.city,
COUNT(t.trip_id) total_trips,
SUM(t.fare) revenue,
AVG(t.fare) avg_fare
FROM customers c
JOIN trips t
ON c.customer_id=t.customer_id
WHERE t.trip_status='Completed'
GROUP BY c.city
order by total_trips;

select * from city_performance;

-- 12. Most Popular Routes

CREATE TABLE popular_routes AS
SELECT
pickup_location,
drop_location,
COUNT(*) trips,
SUM(fare) revenue
FROM trips
WHERE trip_status='Completed'
GROUP BY pickup_location,drop_location
ORDER BY trips DESC;

select*from popular_routes;

-- 13. Top 10 Drivers(Revenue)
CREATE TABLE top_drivers AS
SELECT
driver_id,
COUNT(*) total_trips,
SUM(fare) revenue,
ROUND(AVG(driver_rating),2) rating
FROM trips
WHERE trip_status='Completed'
GROUP BY driver_id
ORDER BY revenue DESC
LIMIT 10;

select*from top_drivers;

-- 14.Top 10 Customers(spending)

CREATE TABLE top_customers AS
SELECT
customer_id,
COUNT(*) total_trips,
SUM(fare) total_spent
FROM trips
WHERE trip_status='Completed'
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;

select * from top_customers;


-- 15. KPI Summary

CREATE TABLE kpi_summary AS
SELECT
COUNT(*) total_trips,
SUM(CASE WHEN trip_status='Completed' THEN fare ELSE 0 END) total_revenue,
ROUND(AVG(fare),2) avg_fare,
ROUND(AVG(distance_km),2) avg_distance,
ROUND(AVG(driver_rating),2) avg_driver_rating,
ROUND(AVG(customer_rating),2) avg_customer_rating,
SUM(CASE WHEN trip_status='Cancelled' THEN 1 ELSE 0 END) cancelled_trips
FROM trips;

select*from kpi_summary;

