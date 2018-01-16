UPDATE TrackUser SET TrackUser.numberOfViews = TrackUser.numberOfViews + 1
WHERE 	TrackUser.userName = "%s" AND
		TrackUser.trackId = (
			SELECT	New_TrackUser.track
            FROM	(
					SELECT 	trackuser.trackId AS track, Songs.trackName AS tName
					FROM 	trackuser, Songs
					WHERE 	Songs.trackName = "%s" AND
							trackuser.userName = "%s" AND
							trackuser.trackId = Songs.trackId) AS New_TrackUser
			WHERE	New_TrackUser.tName = "%s")