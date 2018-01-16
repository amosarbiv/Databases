SELECT	sum(Trackuser.ranking) as Rating, Artists.artistName as 'Artist'
FROM	Trackuser, Songs, Artists, CollectionsArtist
WHERE	TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = CollectionsArtist.collectionId AND
		CollectionsArtist.artistId = Artists.artistId AND
		Songs.trackReleaseDate BETWEEN '1950-01-01' AND '1959-12-31'
GROUP BY Artists.artistName
ORDER BY 1 DESC
LIMIT 5