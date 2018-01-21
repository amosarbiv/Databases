SELECT DbMysql15.Songs.trackId, DbMysql15.Songs.trackName as Song, DbMysql15.Artists.artistName AS Artist, DbMysql15.Collections.collectionName AS Album,
		DbMysql15.TrackUser.ranking AS 'You Rated', DbMysql15.TrackUser.numberOfViews AS 'Plays',
		DbMysql15.Songs.discNumber AS 'Disc Number', DbMysql15.Songs.trackPosition AS 'Track Position', DbMysql15.Songs.trackTimeMillis AS 'Length (msec)',
        convert(DbMysql15.Songs.trackReleaseDate using utf8) AS 'Release Date',
        DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS 'Price ($)', DbMysql15.Songs.previewSong
        FROM DbMysql15.Songs, DbMysql15.Collections, DbMysql15.CollectionsArtist, DbMysql15.Artists, DbMysql15.TrackUser
        WHERE DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
		DbMysql15.Collections.collectionId = DbMysql15.CollectionsArtist.collectionId AND
        DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
        DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
        DbMysql15.TrackUser.userName = '%s' AND
        DbMysql15.TrackUser.isInPlaylist = '1'
        ORDER BY 4 DESC