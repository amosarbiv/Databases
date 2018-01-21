SELECT	DbMysql15.Collections.collectionName AS Album, DbMysql15.Collections.collectionPrice AS 'Price ($)', userPlaylist.artistName, convert(DbMysql15.Collections.collectionReleaseDate using utf8),DbMysql15.Collections.collectionGenre
                FROM	(
		        SELECT	DbMysql15.TrackUser.userName as tempUser, DbMysql15.TrackUser.trackId as track, DbMysql15.Artists.artistId as artistid, DbMysql15.Artists.artistName
		        FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.CollectionsArtist, DbMysql15.Artists
		        WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
				DbMysql15.TrackUser.userName = "AARONBENNETT" AND
				DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
		        ) AS userPlaylist, DbMysql15.Collections, DbMysql15.CollectionsArtist
                WHERE	userPlaylist.artistid = DbMysql15.CollectionsArtist.artistId AND
		        DbMysql15.CollectionsArtist.collectionId = DbMysql15.Collections.collectionId
                ORDER BY 1 ASC
                LIMIT 10