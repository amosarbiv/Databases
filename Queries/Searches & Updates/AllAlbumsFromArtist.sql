SET @userName:="%s"; #
SET @artistId:="%s";
SET @artistCurerentId:=""; 

SELECT  @artistCurerentId:=ArtistId AS ArtistCurrentId,
		Album AS Album, 
		convert(AlbumRelease using utf8) AS AlbumRelease, 
		AlbumPrice AS AlbumPrice, 
        AlbumGenre AS AlbumGenre,
        AlbumCountry AS AlbumCountry,
        AlbumNumberOfTracks AS AlbumNumberOfTracks,
		Artist AS Artist,
		ArtistId AS ArtistId,
        ArtistPrimaryGenre AS ArtistPrimaryGenre,
        artistPicture AS artistPicture,
		CASE
			WHEN (
				SELECT COUNT(artistId) 
                FROM DbMysql15.ArtistUser 
                WHERE DbMysql15.ArtistUser.artistId=@artistCurrentId AND DbMysql15.ArtistUser.userName=@userName) > 0
			THEN (
				SELECT CAST(DbMysql15.ArtistUser.artistRanking AS char)
                FROM DbMysql15.ArtistUser
                WHERE DbMysql15.ArtistUser.artistId=@artistCurrentId AND DbMysql15.ArtistUser.userName=@userName)
			ELSE null 
            END AS paramsInArtistUser
FROM	(SELECT DbMysql15.Collections.collectionName AS Album, 
				DbMysql15.Collections.collectionReleaseDate AS AlbumRelease, 
				DbMysql15.Collections.collectionPrice AS AlbumPrice, 
				DbMysql15.Collections.collectionGenre AS AlbumGenre,
				DbMysql15.Collections.country AS AlbumCountry,
				DbMysql15.Collections.numberOfTracks AS AlbumNumberOfTracks,
				DbMysql15.Artists.artistName AS Artist,
                DbMysql15.Artists.artistId AS ArtistId,
                DbMysql15.Artists.ArtistPrimaryGenre AS ArtistPrimaryGenre,
                DbMysql15.Artists.artistPicture AS artistPicture
		FROM 	DbMysql15.Artists, DbMysql15.Collections, DbMysql15.CollectionsArtist
									 
		WHERE 	DbMysql15.Artists.artistId=@artistId AND
				DbMysql15.CollectionsArtist.artistId = @artistId AND
				DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId) AS nested
                
		ORDER BY AlbumRelease DESC
