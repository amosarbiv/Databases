SET @userName:="%s"; 
SET @trackName:="%s"; 
SET @collectionName:="%s";
SET @songCurerentId:=""; 

SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
		discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,previewSong AS previewSong,
        CASE
			WHEN (
				SELECT COUNT(trackId) 
                FROM TrackUser 
                WHERE trackUser.trackId=@songCurerentId AND trackUser.userName=@userName) > 0
			THEN (
				SELECT concat(CAST(TrackUser.numberOfViews AS char), ",", CAST(TrackUser.ranking AS char), ",", CAST(TrackUser.isInPlaylist AS char))
                FROM TrackUser
                WHERE trackUser.trackId=@songCurerentId AND trackUser.userName=@userName)
			ELSE null 
            END AS paramsInTrackUser
FROM	(SELECT  Songs.trackName AS Song, Songs.trackId AS trackId,
					Collections.collectionName AS Album, 
					Artists.artistName AS Artist, Songs.discNumber AS discNumber, 
					Songs.trackPosition AS trackPosition, 
					Songs.trackTimeMillis AS length, 
					Songs.trackReleaseDate AS releaseDate,
					Songs.trackGenre AS Genre, Songs.trackPrice AS price, Songs.previewSong as previewSong,
					null AS numberOfTracks
		FROM 	Songs, Artists, Collections, CollectionsArtist
									 
		WHERE 	Songs.trackName REGEXP Concat("([ ]|^)", @trackName,"([,. ;]|$)") AND 
				Collections.collectionName REGEXP Concat("([ ]|^)", @collectionName,"([,. ;]|$)") AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = CollectionsArtist.collectionId AND
				CollectionsArtist.artistId = Artists.artistId) AS nested
