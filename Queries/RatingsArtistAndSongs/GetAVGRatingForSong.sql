SELECT DISTINCT TrackUser.trackId, cast(avg(TrackUser.ranking) as signed),
		count(TrackUser.userName) as numOfRankers
        FROM DbMysql15.TrackUser
        group by TrackUser.trackid