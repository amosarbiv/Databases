SET @userName:="EUSEBIODODD"; #
SET @artistId:="0";
SET @artistCurerentId:=""; 

SELECT  @artistCurerentId:=ArtistId AS ArtistCurrentId,
		Album AS Album, 
		AlbumRelease AS AlbumRelease, 
		AlbumPrice AS AlbumPrice, 
        AlbumGenre AS AlbumGenre,
        AlbumCountry AS AlbumCountry,
        AlbumNumberOfTracks AS AlbumNumberOfTracks,
		Artist AS Artist,
		ArtistId AS ArtistId,
        ArtistPrimaryGenre AS ArtistPrimaryGenre,
        Photo AS Photo,
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
				Artists.artistName AS Artist,
                Artists.artistId AS ArtistId,
                Artists.artistPicture AS Photo,
                Artists.ArtistPrimaryGenre AS ArtistPrimaryGenre
		FROM 	Artists, Collections, CollectionsArtist
									 
		WHERE 	Artists.artistId=@artistId AND
				CollectionsArtist.artistId = @artistId AND
				Collections.collectionId = CollectionsArtist.collectionId) AS nested
