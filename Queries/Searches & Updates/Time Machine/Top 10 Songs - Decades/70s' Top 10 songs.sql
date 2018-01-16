SELECT	sum(TrackUser.ranking) as Rating, Songs.trackName as 'Song'
FROM	TrackUser, Songs
WHERE	TrackUser.trackId = Songs.trackId AND
		Songs.trackReleaseDate BETWEEN '1970-01-01' AND '1979-12-31'
GROUP BY Songs.trackName
ORDER BY 1 DESC
LIMIT 10