-- importing database of this table
SELECT `city`, `temperature`
FROM `temperatures`
WHERE month IN (`July`, `August`)
GROUP BY `city`
ORDER BY temperature DESC
LIMIT 3;

