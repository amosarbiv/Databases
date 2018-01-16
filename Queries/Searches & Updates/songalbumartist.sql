
#  This query is used for search query such as:
#  "Love", "Barbra" etc.
# Results can vary and include: Songs, Albums, Artists
# For each result - only the relevant paramters are assigned:
# for example - artist wont include song name - will be null.
# ExtraParams - for songs -- will include ranking, number of views, isinplaylist.
# For artists - will include ranking.

SET @userName:="%s"; # Add username as %s
SET @sQ:="%s"; # Search Query
SET @songCurerentId:=""; # 
SET @artistCurrentId:=""; # 
SELECT  @artistCurrentId:=artistId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
		discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,previewSong AS previewSong,
        CASE
			WHEN (
				SELECT COUNT(artistId) 
                FROM artistuser 
                WHERE artistUser.artistId=@artistCurrentId AND artistUser.userName=@userName) > 0
			THEN (
				SELECT CAST(artistUser.artistRanking AS char)
                FROM artistUser
                WHERE artistUser.artistId=@artistCurrentId AND artistUser.userName=@userName)
			ELSE null 
            END AS ExtraParams
FROM	(SELECT  null AS Song, null AS trackId,
					null AS Album, 
                    Artists.artistId as artistId,
					Artists.artistName AS Artist, null AS discNumber, 
					null AS trackPosition, 
					null AS length, 
					null AS releaseDate,
					Artists.artistPrimaryGenre AS Genre, null AS price,
					null AS numberOfTracks,
                    null as previewSong
		FROM 	Artists
									 
		WHERE 	Artists.artistName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)")) AS nested
UNION
SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
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
            END AS ExtraParams
FROM	(SELECT  	Songs.trackName AS Song, Songs.trackId AS trackId,
					Collections.collectionName AS Album, 
					Artists.artistName AS Artist, Songs.discNumber AS discNumber, 
					Songs.trackPosition AS trackPosition, 
					Songs.trackTimeMillis AS length, 
					Songs.trackReleaseDate AS releaseDate,
					Songs.trackGenre AS Genre, Songs.trackPrice AS price,
					null AS numberOfTracks, Songs.previewSong as previewSong
		FROM 		Artists, Collections, CollectionsArtist, Songs
		WHERE 	Songs.trackName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)") AND
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
        Collections.numberOfTracks AS numberOfTracks,
        null as previewSong,
		null as ExtraParams
FROM 	Artists,Collections, CollectionsArtist
WHERE 	Collections.collectionName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)") AND 
		Collections.collectionId = CollectionsArtist.collectionId AND
        CollectionsArtist.artistId = Artists.artistId;
        
