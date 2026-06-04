SELECT *
FROM housing_data
ORDER BY price DESC
LIMIT 5;

-- Average price by furnishing status
SELECT furnishingstatus, AVG(price) AS avg_price
FROM housing_data
GROUP BY furnishingstatus;

-- Houses with more than 3 bedrooms
SELECT *
FROM housing_data
WHERE bedrooms > 3;

-- Average area by number of bedrooms
SELECT bedrooms, AVG(area) AS avg_area
FROM housing_data
GROUP BY bedrooms;

-- Houses with highest parking spaces
SELECT *
FROM housing_data
ORDER BY parking DESC;