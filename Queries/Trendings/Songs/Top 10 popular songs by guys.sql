SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userGender = 'M' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10