SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userAge > 50 AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10