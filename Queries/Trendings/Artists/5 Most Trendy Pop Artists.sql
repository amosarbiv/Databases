SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Popular DbMysql15.Songs'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.CollectionsArtist, DbMysql15.Artists
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
        DbMysql15.Artists.artistPrimaryGenre = 'Pop'
GROUP BY DbMysql15.Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 5