SET @userName:="%s";
SET @trackName:="%s";
SET @collectionName:="%s";
SET @artistName:="%s"; 
SET @songCurerentId:=""; 

SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
		discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
        Genre AS Genre, price AS price, previewSong, numberOfTracks AS numberOfTracks,
        CASE
			WHEN (
				SELECT COUNT(trackId) 
                FROM DbMysql15.TrackUser 
                WHERE DbMysql15.TrackUser.trackId=@songCurerentId AND DbMysql15.TrackUser.userName=@userName) > 0
			THEN (
				SELECT concat(CAST(DbMysql15.TrackUser.numberOfViews AS char), ",", CAST(DbMysql15.TrackUser.ranking AS char), ",", CAST(DbMysql15.TrackUser.isInPlaylist AS char))
                FROM DbMysql15.TrackUser
                WHERE DbMysql15.TrackUser.trackId=@songCurerentId AND DbMysql15.TrackUser.userName=@userName)
			ELSE null 
            END AS paramsInTrackUser
FROM	(SELECT  DbMysql15.Songs.trackName AS Song, DbMysql15.Songs.trackId AS trackId,
					DbMysql15.Collections.collectionName AS Album, 
					DbMysql15.Artists.artistName AS Artist, DbMysql15.Songs.discNumber AS discNumber, 
					DbMysql15.Songs.trackPosition AS trackPosition, 
					DbMysql15.Songs.trackTimeMillis AS length, 
					DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS price,
                    DbMysql15.Songs.previewSong AS previewSong,
					null AS numberOfTracks
		FROM 	DbMysql15.Songs, DbMysql15.Artists, DbMysql15.Collections, DbMysql15.CollectionsArtist
									 
		WHERE 	DbMysql15.Songs.trackName REGEXP Concat("([ ]|^)", @trackName,"([,. ;]|$)") AND 
				DbMysql15.Artists.artistName REGEXP Concat("([ ]|^)", @artistName,"([,. ;]|$)") AND
				DbMysql15.Collections.collectionName REGEXP Concat("([ ]|^)", @collectionName,"([,. ;]|$)") AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS nested
