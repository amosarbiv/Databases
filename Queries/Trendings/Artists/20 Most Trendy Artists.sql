SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Popular DbMysql15.Songs'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.CollectionsArtist, DbMysql15.Artists
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = CollectionsArtist.collectionId AND
		DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
GROUP BY DbMysql15.Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 20