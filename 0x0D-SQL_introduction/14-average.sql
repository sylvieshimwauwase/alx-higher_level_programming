-- script that computes the score average of all records
SELECT  `score` AS average
FROM second_table
GROUP BY `score`;
