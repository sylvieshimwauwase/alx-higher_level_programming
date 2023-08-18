-- scripts that lists all genres from database
SELECT genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
