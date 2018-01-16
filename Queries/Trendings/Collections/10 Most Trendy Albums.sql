SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 10