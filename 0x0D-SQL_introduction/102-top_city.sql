-- importing database of this table
SELECT `city`, `temperature`
FROM `temperature`
WHERE month IN (`July`, `August`)
ORDER BY temperature DESC
LIMIT 3;

