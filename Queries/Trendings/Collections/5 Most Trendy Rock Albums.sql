SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
        DbMysql15.Collections.collectionGenre = 'Rock'
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5