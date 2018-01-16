SELECT	sum(TrackUser.ranking) as Rating, Songs.trackName as 'Song'
FROM	TrackUser, Songs
WHERE	TrackUser.trackId = Songs.trackId AND
		Songs.trackReleaseDate BETWEEN '%s' AND '%s'
GROUP BY Songs.trackName
ORDER BY 1 DESC
LIMIT 10