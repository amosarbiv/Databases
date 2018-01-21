SELECT	sum(viewsPerTrack.views) as 'Number of Views', trackGenre as '1950s Genre'
                FROM ( 
            	SELECT	sum(numberOfViews) as views, trackId as track
	            FROM	DbMysql15.TrackUser
	            GROUP BY DbMysql15.TrackUser.trackId) as viewsPerTrack, DbMysql15.Songs 
                WHERE	viewsPerTrack.track = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '1960-01-01' AND '1969-12-31'
                GROUP BY DbMysql15.Songs.trackGenre
                ORDER BY 1 DESC
                LIMIT 5