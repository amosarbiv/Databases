SET @userName:="%s"; #EUSEBIODODD
SET @collectionId:="%s";
SET @songCurerentId:="";
SET @artistCurerentId:=""; 

SELECT  @songCurerentId:=trackId AS SongCurrentId,
		@artistCurerentId:=ArtistId AS ArtistCurrentId,
		Album AS Album, 
		AlbumRelease AS AlbumRelease, 
		AlbumPrice AS AlbumPrice, 
        AlbumGenre AS AlbumGenre,
        AlbumCountry AS AlbumCountry,
        AlbumNumberOfTracks AS AlbumNumberOfTracks,
        Song AS Song, SongDiscNumber AS SongDiscNumber,
        SongPositionInDisc AS SongPositionInDisc, 
        SongReleaseDate AS SongReleaseDate,
        SongGenre AS SongGenre,
        SongLength AS SongLength,
        SongPrice AS SongPrice,
        trackId AS trackId,
        isInPlaylist AS isInPlaylist,
        previewSong AS previewSong,
		Artist AS Artist,
		ArtistId AS ArtistId,
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
            END AS paramsInTrackUser,
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
            END AS paramsInArtistUser
FROM	(SELECT Collections.collectionName AS Album, 
				Collections.collectionReleaseDate AS AlbumRelease, 
				Collections.collectionPrice AS AlbumPrice, 
				Collections.collectionGenre AS AlbumGenre,
				Collections.country AS AlbumCountry,
				Collections.numberOfTracks AS AlbumNumberOfTracks,
				Songs.trackName AS Song, Songs.discNumber AS SongDiscNumber,
				Songs.trackPosition AS SongPositionInDisc, 
				Songs.trackReleaseDate AS SongReleaseDate,
				Songs.trackGenre AS SongGenre,
				Songs.trackTimeMillis AS SongLength,
				Songs.trackPrice AS SongPrice,
                Songs.trackId AS trackId,
                Songs.isInPlaylist AS isInPlaylist,
                Songs.previewSong AS previewSong,
				Artists.artistName AS Artist,
                Artists.artistId AS ArtistId
		FROM 	Songs, Artists, Collections, CollectionsArtist
									 
		WHERE 	Collections.collectionId=@collectionId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = CollectionsArtist.collectionId AND
				CollectionsArtist.artistId = Artists.artistId) AS nested
