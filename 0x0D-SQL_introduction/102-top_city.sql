-- importing database of this table
SELECT `city`, AVG(`value`) AS`avg_temperature`
FROM `temperatures`
WHERE month IN (`July`, `August`)
GROUP BY `city`
ORDER BY `avg_temperature` DESC
LIMIT 3;

