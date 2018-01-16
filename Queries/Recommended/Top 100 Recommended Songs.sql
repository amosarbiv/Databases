SELECT	Songs.trackName as Song, sum(TrackUser.ranking) as 'Users Rated'
FROM	(
		SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artist
		FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "%s" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId
		) AS userPlaylist, Songs, TrackUser, Collections, collectionsartist

WHERE	userPlaylist.artist = collectionsartist.artistId AND
		collectionsartist.collectionId = Collections.collectionId AND
		Collections.collectionId = Songs.collectionId AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC
LIMIT 100