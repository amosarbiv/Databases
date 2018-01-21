SELECT	DbMysql15.Songs.trackName as Song,cast(avg(DbMysql15.TrackUser.ranking) as signed) AS Rating, DbMysql15.Songs.trackId, userPlaylist.numOfSongs as numOfSongs, DbMysql15.Collections.collectionName AS Album, DbMysql15.Artists.artistName AS Artist,
		DbMysql15.Songs.previewSong AS Preview, DbMysql15.Songs.trackId AS 'Track ID',
		DbMysql15.Songs.trackGenre AS Genre,convert(DbMysql15.Songs.trackReleaseDate using utf8) AS 'Release Date', DbMysql15.Songs.trackPrice AS Price
        FROM	(
		SELECT	DISTINCT DbMysql15.TrackUser.userName as tempUser, count(DbMysql15.TrackUser.trackId) as numOfSongs, DbMysql15.Artists.artistId as artist, DbMysql15.TrackUser.trackId as track
		FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.CollectionsArtist, DbMysql15.Artists
		WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.userName = "%s" AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
		DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
		GROUP BY DbMysql15.Artists.artistId
		) AS userPlaylist, DbMysql15.Songs, DbMysql15.TrackUser, DbMysql15.Collections, DbMysql15.CollectionsArtist, DbMysql15.Artists
        WHERE	DbMysql15.Artists.artistId = userPlaylist.artist AND
		DbMysql15.TrackUser.isInPlaylist='0' AND
        DbMysql15.Songs.trackId NOT IN (SELECT DbMysql15.TrackUser.trackId FROM DbMysql15.TrackUser WHERE DbMysql15.TrackUser.userName = "%s" AND DbMysql15.TrackUser.isInPlaylist = '1') AND
		userPlaylist.artist = DbMysql15.CollectionsArtist.artistId AND
		DbMysql15.CollectionsArtist.collectionId = DbMysql15.Collections.collectionId AND
		DbMysql15.Collections.collectionId = DbMysql15.Songs.collectionId AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
        GROUP BY DbMysql15.TrackUser.trackId
        ORDER BY 2 DESC
        LIMIT 100