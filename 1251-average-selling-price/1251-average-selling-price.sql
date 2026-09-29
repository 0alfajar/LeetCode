# Write your MySQL query statement below
SELECT 
    p.product_id,
    IFNULL(round(SUM(u.units * p.price) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
    ON u.product_id = p.product_id AnD u.purchase_date BETWEEN p.Start_date and p.end_date
GROUP BY product_Id
ORDER BY product_id