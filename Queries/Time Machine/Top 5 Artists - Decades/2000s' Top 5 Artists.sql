SELECT	sum(Trackuser.ranking) as Rating, Artists.artistName as 'Artist'
FROM	Trackuser, Songs, Artists, CollectionsArtist
WHERE	TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = CollectionsArtist.collectionId AND
		CollectionsArtist.artistId = Artists.artistId AND
		Songs.trackReleaseDate BETWEEN '2000-01-01' AND '2009-12-31'
GROUP BY Artists.artistName
ORDER BY 1 DESC
LIMIT 5