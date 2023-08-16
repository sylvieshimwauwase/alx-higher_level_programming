-- script that lists number of records with teh same score
SELECT COUNT(`score`)
FROM second_table
ORDER BY `score` DESC;
