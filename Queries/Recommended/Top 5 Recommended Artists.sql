SELECT	Artists.artistName as Artist, count(userPlaylist.track) as 'Number of Songs You Like of This Artist',
		Artists.artistId AS 'Artist ID'
FROM	(
		SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artist
		FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "%s" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId) AS userPlaylist, Artists
WHERE	userPlaylist.artist = Artists.artistId
GROUP BY userPlaylist.artist
ORDER BY 2 DESC
LIMIT 5