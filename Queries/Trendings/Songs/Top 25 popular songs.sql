SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Fond DbMysql15.Users'
FROM	DbMysql15.TrackUser, DbMysql15.Songs
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 25