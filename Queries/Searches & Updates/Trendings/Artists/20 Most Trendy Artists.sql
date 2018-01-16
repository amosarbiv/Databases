SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number of Popular Songs'
FROM	TrackUser, Songs, Collectionsartist, Artists
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId
GROUP BY Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 20