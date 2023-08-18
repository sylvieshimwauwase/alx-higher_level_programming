-- scripts that lists all cities of california found in database
SELECT cities.name
FROM cities, states
WHERE cities.state_id = (SELECTid FROM states WHERE name = 'California')
AND cities.state_id = states.id
ORDER BY cities.id ASC;
