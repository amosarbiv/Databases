SELECT	DbMysql15.Artists.artistName as Artist, count(userPlaylist.track) as 'Number of DbMysql15.Songs You Like of This Artist',
		        DbMysql15.Artists.artistPrimaryGenre AS 'Artist Genre'
                FROM	(
		        SELECT	DbMysql15.TrackUser.userName as tempUser, DbMysql15.TrackUser.trackId as track, DbMysql15.Artists.artistId as artist
		        FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.CollectionsArtist, DbMysql15.Artists
		        WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
				DbMysql15.TrackUser.userName = "%s" AND
				DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS userPlaylist, DbMysql15.Artists
                WHERE	userPlaylist.artist = DbMysql15.Artists.artistId
                GROUP BY userPlaylist.artist
                ORDER BY 2 DESC
                LIMIT 5