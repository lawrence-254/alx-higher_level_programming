-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.name FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id = sg.show_id
INNER JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
