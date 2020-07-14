-- Number of records with same score
-- SELECT GROUP
SELECT score AS `score`,
       COUNT(score) as `number`
FROM second_table
GROUP BY score
ORDER BY score DESC;
