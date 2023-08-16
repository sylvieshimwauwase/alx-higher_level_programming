-- script that displays max temperature
SELECT `state`, MAX(`temperature`) AS max_temperature
FROM `temperature`
GROUP BY `state`
ORDER BY `state`;`
