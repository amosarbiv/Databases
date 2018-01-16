SELECT	sum(viewsPerTrack.views) as 'Number of Views', trackGenre as '1950s Genre', Songs.trackReleaseDate
FROM ( 
	SELECT	sum(numberOfViews) as views, trackId as track
	FROM	TrackUser
	GROUP BY TrackUser.trackId) as viewsPerTrack, Songs 
WHERE	viewsPerTrack.track = Songs.trackId AND
		Songs.trackReleaseDate BETWEEN '%s' AND '%s'
GROUP BY Songs.trackGenre
ORDER BY 1 DESC
LIMIT 5