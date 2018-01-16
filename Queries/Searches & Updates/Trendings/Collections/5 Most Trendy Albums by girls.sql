SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections, Users
WHERE	Users.userGender = 'F' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5