-- script that lists number of records with teh same score
SELECT `score`, COUNT(*) AS `number`
FROM second_table
GROUP BY `score`
ORDER BY `number` DESC;
