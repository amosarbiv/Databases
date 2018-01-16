UPDATE ArtistUser SET artistRanking = "%s"
WHERE	(SELECT Artists.artistId FROM Artists WHERE Artists.artistName = "%s") AND
		ArtistUser.userName = "%s"