SELECT	sum(DbMysql15.TrackUser.ranking) as Rating, DbMysql15.Songs.trackName as 'Song'
                FROM	DbMysql15.TrackUser, DbMysql15.Songs
                WHERE	DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '1990-01-01' AND '1999-12-31'
                GROUP BY DbMysql15.Songs.trackName
                ORDER BY 1 DESC
                LIMIT 5