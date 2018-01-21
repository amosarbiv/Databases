SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.CollectionsArtist, DbMysql15.Artists, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'M' AND
        DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
GROUP BY DbMysql15.Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10