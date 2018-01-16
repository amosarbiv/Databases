SELECT DISTINCT artistuser.artistId, avg(artistuser.artistRanking) as ranking,
		count(artistUser.userName) as numOfRankers
        FROM artistUser
        group by artistUser.artistId