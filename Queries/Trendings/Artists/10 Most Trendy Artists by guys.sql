SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	TrackUser, Songs, Collectionsartist, Artists, Users
WHERE	Users.userGender = 'M' AND
        Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId
GROUP BY Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10