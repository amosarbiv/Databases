SELECT	sum( ArtistsAndGenres.artistName As "Artist", ArtistsAndGenres.popularGenre AS "Genre"
FROM	(
		SELECT	sum(Views.numOfViews) AS views, Artists.artistName, Songs.primaryGenreName AS popularGenre
		FROM	Songs, Views, Artists, Artist_Song
		WHERE	Songs.trackId = Views.trackId,
				Views.trackId = Artist_Song.trackId,
				Artist_Song.artistId = Artists.artistId
				GROUP BY Views.trackId
		) ArtistsAndGenres
                