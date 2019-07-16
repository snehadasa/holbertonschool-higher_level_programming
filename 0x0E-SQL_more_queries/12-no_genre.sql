-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_showd.id=tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genre.genre_is;
