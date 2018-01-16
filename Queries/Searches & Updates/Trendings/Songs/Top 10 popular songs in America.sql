SELECT	count(TrackUser.isInPlaylist) as 'Number of Appearances', Songs.trackName as 'Song'
FROM	TrackUser, Users, Songs
WHERE	TrackUser.userId = Users.userId AND
		Songs.trackId = TrackUser.trackId AND
		TrackUser.isInPlaylist = '1' AND
        Users.userCountry = 'United States'
GROUP BY TrackUser.trackId
ORDER BY 1 DESC
LIMIT 10