SET @userName:="%s"; 
SET @AlbumOrSong:="%s";
SET @Artist:="%s";
SET @songCurerentId:="";

SELECT  @songCurerentId:=trackId, Song AS Song, Album AS Album, Artist AS Artist,
		discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks, previewSong as previewSong,
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
					Songs.trackGenre AS Genre, Songs.trackPrice AS price,
					null AS numberOfTracks, Songs.previewSong as previewSong
		FROM 	Songs, Artists, Collections, CollectionsArtist
									 
		WHERE 	Songs.trackName REGEXP Concat("([ ]|^)", @AlbumOrSong,"([,. ;]|$)") AND 
									Artists.artistName REGEXP Concat("([ ]|^)", @Artist,"([,. ;]|$)")  AND 
									Songs.collectionId = Collections.collectionId AND
									Collections.collectionId = CollectionsArtist.collectionId AND
									CollectionsArtist.artistId = Artists.artistId) AS nested
UNION
SELECT 	Collections.collectionId AS currentId, null AS Song, Collections.collectionName AS Album, 
		Artists.artistName AS Artist, null AS discNumber, 
        null AS trackPosition, 
        null AS length, 
        Collections.collectionReleaseDate AS releaseDate,
        Collections.collectionGenre AS genre,
        Collections.collectionPrice AS price,
        Collections.numberOfTracks AS numberOfTracks, null as previewSong,
        null as paramsInTrackUser
FROM 	Artists,Collections, CollectionsArtist
WHERE 	Collections.collectionName REGEXP Concat("([ ]|^)", @AlbumOrSong,"([,. ;]|$)") AND 
		Artists.artistName REGEXP Concat("([ ]|^)", @Artist,"([,. ;]|$)")  AND 
        Collections.collectionId = CollectionsArtist.collectionId AND
        CollectionsArtist.artistId = Artists.artistId
