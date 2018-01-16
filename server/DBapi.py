import MySQLdb as sql
import logging
import os
import json

artistTrending = [
    """SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number of Popular Songs'
FROM	TrackUser, Songs, Collectionsartist, Artists
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId
GROUP BY Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 20""",
"""SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	TrackUser, Songs, Collectionsartist, Artists, Users
WHERE	Users.userGender = 'F' AND
        Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId
GROUP BY Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	TrackUser, Songs, Collectionsartist, Artists, Users
WHERE	Users.userGender = 'M' AND
        Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId
GROUP BY Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number of Popular Songs'
FROM	TrackUser, Songs, Collectionsartist, Artists
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId AND
        Artists.artistPrimaryGenre = 'Pop'
GROUP BY Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	Artists.artistName as Artist, count(TrackUser.isInPlaylist) as 'Number of Popular Songs'
FROM	TrackUser, Songs, Collectionsartist, Artists
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collectionsartist.collectionId AND
		Collectionsartist.artistId = Artists.artistId AND
        Artists.artistPrimaryGenre = 'Rock'
GROUP BY Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 5"""
]

songTrending = [
    """SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Fond Users'
FROM	TrackUser, Songs
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 25""",
"""SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userGender = 'F' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userGender = 'M' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userAge > 50 AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userAge BETWEEN '30' AND '49' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Songs.trackName as Song, count(TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	TrackUser, Songs, Users
WHERE	Users.userAge BETWEEN '0' AND '29' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId
GROUP BY TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10"""
]

collectionTrending = [
    """SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections, Users
WHERE	Users.userGender = 'F' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections, Users
WHERE	Users.userGender = 'M' AND
		Users.userName = TrackUser.userName AND
		TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId AND
        Collections.collectionGenre = 'Pop'
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	Collections.collectionName as Album, count(TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	TrackUser, Songs, Collections
WHERE	TrackUser.isInPlaylist = '1' AND
		TrackUser.trackId = Songs.trackId AND
		Songs.collectionId = Collections.collectionId AND
        Collections.collectionGenre = 'Rock'
GROUP BY Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5"""
]

class DB():
    def __init__(self, DBUserName, DBPasswd, DBName, DBPort=3306, DBhost="127.0.0.1"):

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("DBapi")
        
        try:
            self.DB = sql.connect(host=DBhost,
                                    user=DBUserName,
                                    passwd=DBPasswd,
                                    db=DBName,
                                    port=DBPort)
        except Exception as e:
            self.logger.error("Error in logging to DB: %s"%str(e))
            os._exit(0)
        
        self.cur = self.DB.cursor() 

    def CreateUser(self, user, password, firstName, lastName, age, country, radioButton):
        userExist = self.CheckUserExists(user)
        if(userExist == False):
            return False
        else:
            query = "INSERT INTO test.users (userName, userPassword, userFirstName, userLastName, userCountry, userGender, userAge, playlistPrivacy) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {});".format(user, password, firstName, lastName, country, radioButton, age, 1)
            try:
                self.cur.execute(query)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return False
    
    def CheckUserExists(self,user):
        query = "SELECT users.userName FROM users WHERE users.userName='%s'"%user
        self.cur.execute(query)
        results = self.cur.fetchall()
        if ( len(results) == 0 ):
            return True #meaning no such user
        else:
            return False


    def UpdateUserProfile(self, user, password, firstName, lastName, country, age):
        query = "UPDATE test.users SET userPassword='{}', userFirstName='{}', userLastName='{}', userCountry='{}', userAge={} WHERE userName='{}';".format(password, firstName, lastName, country, age, user)
        try:
            self.cur.execute(query)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return False

    def MakeJsonUserDetails(self,user):
        query = "SELECT * FROM users WHERE users.userName='%s'"%user
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            (userName, password,firstName,lastName,country,gender,age,privacy) = results[0]
            dic = {"UserName":userName,"Password":password,"FirstName":firstName,"LastName":lastName,"Country":country,"Age":age,"PlaylistPrivacy":privacy}
            f = open("server//tmpFiles//userProfile.json","w")
            json.dump(dic, f)
            f.close() 
            return True
        except:
            self.DB.rollback()
            return False

    def CheckUserLogin(self, userName, password):
        query = "SELECT users.userName, users.userPassword FROM users WHERE users.userName='%s'"%userName
        self.cur.execute(query)
        results = self.cur.fetchall()
        if ( len(results) == 0 ):
            return False #meaning no such user 

        (user, passwd) = results[0]
        if ( password == passwd ):
            return True
        else:
            return False

    def UpdatePrivacy(self, privacy, user):
        query = "UPDATE test.users SET playlistPrivacy={} WHERE userName='{}';".format(privacy, user)
        try:
            self.cur.execute(query)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return {}

    def getPlayList(self, user):
        query = "SELECT Songs.trackId, Songs.trackName as Song, Artists.artistName AS Artist, Collections.collectionName AS Album,\
		trackUser.ranking AS 'You Rated', trackUser.numberOfViews AS 'Plays',\
		Songs.discNumber AS 'Disc Number', Songs.trackPosition AS 'Track Position', Songs.trackTimeMillis AS 'Length (msec)',\
        convert(Songs.trackReleaseDate using utf8) AS 'Release Date',\
        Songs.trackGenre AS Genre, Songs.trackPrice AS 'Price ($)'\
        FROM Songs, Collections, collectionsartist, Artists, trackUser\
        WHERE Songs.collectionId = collections.collectionId AND\
		collections.collectionId = collectionsartist.collectionId AND\
        collectionsartist.artistId = Artists.artistId AND\
        trackUser.trackId = Songs.trackId AND\
        trackUser.userName = '%s' AND\
        trackUser.isInPlaylist = '1'\
        ORDER BY 4 DESC"%user
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            return False

    def AddSongToPlaylist(self, user, songId):
        query2 = "SELECT * FROM test.trackuser where trackuser.userName = '%s' and trackuser.trackId = '%s';"%(user, songId)
        try:
            self.cur.execute(query2)
            results = self.cur.fetchall()
            if(len(results) != 0):
                query2 = "UPDATE `test`.`trackuser` SET `isInPlaylist`=1 WHERE `trackId`='%s' and`userName`='%s';"%(songId, user)
                try:
                    self.cur.execute(query2)
                    self.DB.commit()
                    return True
                except:
                    self.DB.rollback()
                    return {}
        except:
            self.DB.rollback()
            return {}
        query2 = "INSERT INTO test.trackuser (trackId, userName, numberOfViews, ranking, isInPlaylist)\
             VALUES ('%s', '%s', '%s', '%s', %d);"%(songId, user, 0, 0, 1)
        try:
            self.cur.execute(query2)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return {}

    def changeRating(self, user, rating, songId,isInPlaylist):
        query1 = "SELECT TrackUser.ranking = '%s'\
        WHERE TrackUser.userName = '%s' AND\
		TrackUser.trackId = '%s'"%(rating, user, songId)
        try:
            self.cur.execute(query1)
            results = self.cur.fetchall()
        except:
            self.DB.rollback()
            return {}
        if(len(results) == 0):
            query2 = "INSERT INTO test.trackuser (trackId, userName, numberOfViews, ranking, isInPlaylist)\
             VALUES ('%s', '%s', '%s', '%s', %d);"%(songId, user, 0, ranking,isInPlaylist)
            try:
                self.cur.execute(query2)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return {}
        else:
            query2 = "UPDATE TrackUser SET TrackUser.ranking = '%s'\
            WHERE TrackUser.userName = '%s' AND\
            TrackUser.trackId = '%s'"%(rating, user, songId)
            try:
                self.cur.execute(query2)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return {}

    def GetArtistTableTimeMachine(self,decadeStart,decadeEnd):
        query = """SELECT	sum(Trackuser.ranking) as Rating, Artists.artistName as 'Artist'
                FROM	Trackuser, Songs, Artists, CollectionsArtist
                WHERE	TrackUser.trackId = Songs.trackId AND
		        Songs.collectionId = CollectionsArtist.collectionId AND
		        CollectionsArtist.artistId = Artists.artistId AND
		        Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY Artists.artistName
                ORDER BY 1 DESC
                LIMIT 5""".format(decadeStart,decadeEnd)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}
    
    def GetSongTableTimeMachine(self,decadeStart,decadeEnd):
        query = """SELECT	sum(TrackUser.ranking) as Rating, Songs.trackName as 'Song'
                FROM	TrackUser, Songs
                WHERE	TrackUser.trackId = Songs.trackId AND
		        Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY Songs.trackName
                ORDER BY 1 DESC
                LIMIT 5""".format(decadeStart,decadeEnd)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    

    def GetGenreTableTimeMachine(self,decadeStart,decadeEnd):
        query = """SELECT	sum(viewsPerTrack.views) as 'Number of Views', trackGenre as '1950s Genre'
                FROM ( 
            	SELECT	sum(numberOfViews) as views, trackId as track
	            FROM	TrackUser
	            GROUP BY TrackUser.trackId) as viewsPerTrack, Songs 
                WHERE	viewsPerTrack.track = Songs.trackId AND
		        Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY Songs.trackGenre
                ORDER BY 1 DESC
                LIMIT 5""".format(decadeStart,decadeEnd)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedSongs(self,user):
        query = """SELECT	Songs.trackName as Song, convert(sum(TrackUser.ranking),signed) as 'Users Rated', Collections.collectionName, convert(Songs.trackReleaseDate using utf8), Songs.trackGenre, Songs.trackPrice, userPlaylist.artistName
                FROM	(
		        SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artist,Artists.artistName
		        FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		        WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "{}" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId
		        ) AS userPlaylist, Songs, TrackUser, Collections, collectionsartist
                WHERE	userPlaylist.artist = collectionsartist.artistId AND
		        collectionsartist.collectionId = Collections.collectionId AND
		        Collections.collectionId = Songs.collectionId AND
		        TrackUser.trackId = Songs.trackId
                GROUP BY TrackUser.trackId
                ORDER BY 2 DESC
                LIMIT 50
                """.format(user)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedCollections(self,user):
        query = """SELECT	Collections.collectionName AS Album, Collections.collectionPrice AS 'Price ($)', userPlaylist.artistName, convert(Collections.collectionReleaseDate using utf8),Collections.collectionGenre
                FROM	(
		        SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artistid, Artists.artistName
		        FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		        WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "{}" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId
		        ) AS userPlaylist, Collections, collectionsartist
                WHERE	userPlaylist.artistid = collectionsartist.artistId AND
		        collectionsartist.collectionId = Collections.collectionId
                ORDER BY 1 ASC
                LIMIT 10        
                """.format(user)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedArtists(self,user):
        query = """SELECT	Artists.artistName as Artist, count(userPlaylist.track) as 'Rated', Artists.artistPrimaryGenre
                FROM	(
		        SELECT	TrackUser.userName as tempUser, TrackUser.trackId as track, Artists.artistId as artist
		        FROM	TrackUser, Songs, Collections, collectionsartist, Artists
		        WHERE	TrackUser.isInPlaylist = '1' AND
				TrackUser.userName = "{}" AND
				TrackUser.trackId = Songs.trackId AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = collectionsartist.collectionId AND
				collectionsartist.artistId = Artists.artistId) AS userPlaylist, Artists
                WHERE	userPlaylist.artist = Artists.artistId
                GROUP BY userPlaylist.artist
                ORDER BY 2 DESC
                LIMIT 5
                """.format(user)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def RetrieveAllTypes(self, userName, allType):
        try:
            newQ='SET @userName:=%s;'
            value=("'%s'"%userName)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @sQ:=%s;'
            value=("'%s'"%allType)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @songCurerentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @artistCurrentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ="""
                SELECT  @artistCurrentId:=artistId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
                        discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
                        convert(releaseDate using utf8), Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
                                    null AS numberOfTracks
                        FROM 	Artists
                                                    
                        WHERE 	LOWER(Artists.artistName) LIKE Concat("%", LOWER(@sQ), "%")) AS nested
                UNION
                SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
                        discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
                        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
                FROM	(SELECT  Songs.trackName AS Song, Songs.trackId AS trackId,
                                    Collections.collectionName AS Album, 
                                    Artists.artistName AS Artist, Songs.discNumber AS discNumber, 
                                    Songs.trackPosition AS trackPosition, 
                                    Songs.trackTimeMillis AS length, 
                                    Songs.trackReleaseDate AS releaseDate,
                                    Songs.trackGenre AS Genre, Songs.trackPrice AS price,
                                    null AS numberOfTracks
                        FROM 	Songs, Artists, Collections, CollectionsArtist
                                                    
                        WHERE 	LOWER(Songs.trackName) LIKE Concat("%", LOWER(@sQ), "%") AND 
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
                        null as paramsInTrackUser
                FROM 	Artists,Collections, CollectionsArtist
                WHERE 	LOWER(Collections.collectionName) LIKE Concat("%", LOWER(@sQ), "%") AND 
                        Collections.collectionId = CollectionsArtist.collectionId AND
                        CollectionsArtist.artistId = Artists.artistId
                    """
            self.cur.execute(newQ)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def RetrieveSongAlbum(self, userName, song, album):
        try:
            newQ='SET @userName:=%s;'
            value=("'%s'"%userName)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @trackName:=%s;'
            value=("'%s'"%song)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @collectionName:=%s;'
            value=("'%s'"%album)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @songCurerentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @artistCurrentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ="""
                SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
		        discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
                convert(releaseDate using utf8), Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
					null AS numberOfTracks
		        FROM 	Songs, Artists, Collections, CollectionsArtist
									 
        		WHERE 	LOWER(Songs.trackName) LIKE Concat("%", LOWER(@trackName), "%") AND 
				LOWER(Collections.collectionName) LIKE Concat("%", LOWER(@collectionName), "%") AND
				Songs.collectionId = Collections.collectionId AND
				Collections.collectionId = CollectionsArtist.collectionId AND
				CollectionsArtist.artistId = Artists.artistId) AS nested
                """
            self.cur.execute(newQ)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def RetrieveSongORAlbumArtist(self, userName, songORalbum, artist):
        try:
            newQ='SET @userName:=%s;'
            value=("'%s'"%userName)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @AlbumOrSong:=%s;'
            value=("'%s'"%songORalbum)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @Artist:=%s;'
            value=("'%s'"%artist)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @songCurerentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @artistCurrentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ="""
                SELECT  @songCurerentId:=trackId, Song AS Song, Album AS Album, Artist AS Artist,
                        discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
                        convert(releaseDate using utf8), Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
                                    null AS numberOfTracks
                        FROM 	Songs, Artists, Collections, CollectionsArtist
                                                    
                        WHERE 	LOWER(Songs.trackName) LIKE Concat("%", LOWER(@AlbumOrSong), "%") AND 
                                                    LOWER(Artists.artistName) LIKE Concat("%", LOWER(@Artist), "%")  AND 
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
                        null as paramsInTrackUser
                FROM 	Artists,Collections, CollectionsArtist
                WHERE 	LOWER(Collections.collectionName) LIKE Concat("%", LOWER(@AlbumOrSong), "%") AND 
                        Collections.collectionId = CollectionsArtist.collectionId AND
                        CollectionsArtist.artistId = Artists.artistId
                """
            self.cur.execute(newQ)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def RetrieveSongAlbumArtist(self, userName, song, album, artist):
        try:
            newQ='SET @userName:=%s;'
            value=("'%s'"%userName)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @trackName:=%s;'
            value=("'%s'"%song)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @collectionName:=%s;'
            value=("'%s'"%album)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @artistName:=%s;'
            value=("'%s'"%artist)
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @songCurerentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ='SET @artistCurrentId:=%s;'
            value=("''")
            self.cur.execute(newQ % value)
            self.DB.commit()

            newQ="""
                SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
                        discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
                        convert(releaseDate using utf8), Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
                                    null AS numberOfTracks
                        FROM 	Songs, Artists, Collections, CollectionsArtist
                                                    
                        WHERE 	LOWER(Songs.trackName) LIKE Concat("%", LOWER(@trackName), "%") AND 
                                LOWER(Artists.artistName) LIKE Concat("%", LOWER(@artistName), "%") AND
                                LOWER(Collections.collectionName) LIKE Concat("%", LOWER(@collectionName), "%") AND
                                Songs.collectionId = Collections.collectionId AND
                                Collections.collectionId = CollectionsArtist.collectionId AND
                                CollectionsArtist.artistId = Artists.artistId) AS nested
                """
            self.cur.execute(newQ)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetArtistTableTrending(self, indexTypeOfSearch):
        query = artistTrending[indexTypeOfSearch]
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetSongTableTrending(self, indexTypeOfSearch):
        query = songTrending[indexTypeOfSearch]
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}
    
    def GetCollectionTableTrending(self, indexTypeOfSearch):
        query = collectionTrending[indexTypeOfSearch]
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}