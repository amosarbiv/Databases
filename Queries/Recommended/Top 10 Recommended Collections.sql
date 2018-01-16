SELECT	Collections.collectionName AS Album, Collections.collectionPrice AS 'Price ($)'
FROM	(
		SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artist
		FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "%s" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId
		) AS userPlaylist, Collections, collectionsartist
WHERE	userPlaylist.artist = collectionsartist.artistId AND
		collectionsartist.collectionId = Collections.collectionId
ORDER BY 1 ASC
LIMIT 10