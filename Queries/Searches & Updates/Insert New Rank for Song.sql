INSERT INTO TrackUser (trackId, userName, numberOfViews, ranking, isInPlaylist)
VALUES	(
		(SELECT	Songs.trackId AS track
		FROM 	Songs, collections, collectionsartist, Artists
		WHERE 	Songs.trackName = "%s" AND
				Songs.collectionId = collections.collectionId AND
				collections.collectionName = "%s" AND
				collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId)
		 , "%s", 1, "%s", 0)