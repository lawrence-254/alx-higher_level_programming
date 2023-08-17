-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
USE hbtn_0d_tvshows;
SELECT g.name AS genre, COUNT(gs.genre_id) AS number_of_shows
FROM tv_shows s INNER JOIN tv_show_genres gs
  ON s.id = gs.show_id
  INNER JOIN tv_genres g
  ON gs.genre_id = g.id
GROUP BY g.name
ORDER BY COUNT(gs.genre_id) desc;
