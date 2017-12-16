SELECT	popularGenres.popularGenre AS "Most Popular Genre"
FROM	(
		SELECT	sum(Views.numOfViews) AS views, Songs.primaryGenreName AS popularGenre
		FROM	Songs, Views
		WHERE	Songs.trackId = Views.trackId
				GROUP BY Views.trackId
		) popularGenres
WHERE	popularGenres.popularGenre IN (
		SELECT	max(popularGenres_COPY.views)
        FROM	(
				SELECT	sum(Views.numOfViews) AS views, Songs.primaryGenreName AS popularGenre
				FROM	Songs, Views
				WHERE	Songs.trackId = Views.trackId
						GROUP BY Views.trackId
				) popularGenres_COPY )