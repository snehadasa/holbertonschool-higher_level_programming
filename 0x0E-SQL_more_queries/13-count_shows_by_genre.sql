-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY nuber_of_shows DESC;
