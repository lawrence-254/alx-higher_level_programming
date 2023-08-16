-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as temp
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY temp DESC
LIMIT 3;
