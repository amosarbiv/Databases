SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Fond Users'
FROM	TrackUser, Songs
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 25