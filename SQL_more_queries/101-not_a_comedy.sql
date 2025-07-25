-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
-- Uses a maximum of two SELECT statements

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id != (
    SELECT id
    FROM tv_genres
    WHERE name = 'Comedy'
) OR tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title;
