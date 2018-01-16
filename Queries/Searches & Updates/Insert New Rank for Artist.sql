INSERT INTO ArtistUser (userName, artistId, artistRanking)
VALUES("%s", (SELECT Artists.artistId FROM Artists WHERE Artists.artistName = "%s"), "%s")