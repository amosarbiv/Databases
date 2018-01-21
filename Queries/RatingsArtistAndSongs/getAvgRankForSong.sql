SELECT DISTINCT trackuser.trackId, avg(trackuser.ranking) as ranking,
		count(trackuser.userName) as numOfRankers
        FROM trackuser
        group by trackuser.trackid