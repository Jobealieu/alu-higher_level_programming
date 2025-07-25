-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
-- Uses a maximum of two SELECT statements

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.tv_show_id
    FROM tv_show_genres
    WHERE tv_show_genres.genre_id = (
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
)
ORDER BY tv_shows.title;
