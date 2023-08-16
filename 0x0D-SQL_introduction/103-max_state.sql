-- script that displays max temperature
SELECT `state`, MAX(`temperature`) AS max_temperature
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;`
