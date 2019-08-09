-- script that displays the avg temp by city ordered by temp.
-- script that displays the avg temp by city ordered by temp.
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
