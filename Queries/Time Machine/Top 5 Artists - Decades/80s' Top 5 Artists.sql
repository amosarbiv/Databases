SELECT	sum(DbMysql15.TrackUser.ranking) as Rating, DbMysql15.Artists.artistName as 'Artist'
                FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Artists, DbMysql15.CollectionsArtist
                WHERE	DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.collectionId = DbMysql15.CollectionsArtist.collectionId AND
		        DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '1980-01-01' AND '1989-12-31'
                GROUP BY DbMysql15.Artists.artistName
                ORDER BY 1 DESC
                LIMIT 5