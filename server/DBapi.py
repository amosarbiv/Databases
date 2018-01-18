import pymysql as sql
import logging
import os
import json

artistTrending = [
    """SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Popular DbMysql15.Songs'
FROM	DbMysql15.DbMysql15.TrackUser, DbMysql15.DbMysql15.Songs, DbMysql15.DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.DbMysql15.Artists
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
GROUP BY DbMysql15.Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 20""",
"""SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'F' AND
        DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
GROUP BY DbMysql15.Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number Male Playlists'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'M' AND
        DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
GROUP BY DbMysql15.Artists.artistName
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Popular DbMysql15.Songs'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
        DbMysql15.Artists.artistPrimaryGenre = 'Pop'
GROUP BY DbMysql15.Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	DbMysql15.Artists.artistName as Artist, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Popular DbMysql15.Songs'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
        DbMysql15.Artists.artistPrimaryGenre = 'Rock'
GROUP BY DbMysql15.Artists.artistId
ORDER BY 2 DESC, 1 ASC
LIMIT 5"""
]

songTrending = [
    """SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Fond DbMysql15.Users'
FROM	DbMysql15.TrackUser, DbMysql15.Songs
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 25""",
"""SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'F' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'M' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userAge > 50 AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userAge BETWEEN '30' AND '49' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Songs.trackName as Song, count(DbMysql15.TrackUser.isInPlaylist) as 'Number of Appearances'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Users
WHERE	DbMysql15.Users.userAge BETWEEN '0' AND '29' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC, 1 ASC
LIMIT 10"""
]

collectionTrending = [
    """SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 10""",
"""SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'F' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.Users
WHERE	DbMysql15.Users.userGender = 'M' AND
		DbMysql15.Users.userName = DbMysql15.TrackUser.userName AND
		DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
        DbMysql15.Collections.collectionGenre = 'Pop'
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5""",
"""SELECT	DbMysql15.Collections.collectionName as Album, count(DbMysql15.TrackUser.isInPlaylist) as 'Numbers of Appearences'
FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections
WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
        DbMysql15.Collections.collectionGenre = 'Rock'
GROUP BY DbMysql15.Collections.collectionId
ORDER BY 2 DESC, 1 ASC
LIMIT 5"""
]

class DB():
    def __init__(self, DBUserName, DBPasswd, DBName, DBPort=3306, DBhost="mysqlsrv.cs.tau.ac.il"):

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("DBapi")
        
        try:
            self.DB = sql.connect(host=DBhost,
                                    user=DBUserName,
                                    passwd=DBPasswd,
                                    db=DBName)
        except Exception as e:
            self.logger.error("Error in logging to DB: %s"%str(e))
            os._exit(0)
        
        self.cur = self.DB.cursor() 

    def CreateUser(self, user, password, firstName, lastName, age, country, radioButton):
        userExist = self.CheckUserExists(user)
        if(userExist == False):
            return False
        else:
            query = "INSERT INTO DbMysql15.DbMysql15.Users (userName, userPassword, userFirstName, userLastName, userCountry, userGender, userAge, playlistPrivacy) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {});".format(user, password, firstName, lastName, country, radioButton, age, 1)
            try:
                self.cur.execute(query)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return False
    
    def CheckUserExists(self,user):
        query = "SELECT DbMysql15.Users.userName FROM DbMysql15.DbMysql15.Users WHERE DbMysql15.Users.userName='%s'"%user
        self.cur.execute(query)
        results = self.cur.fetchall()
        if ( len(results) == 0 ):
            return True #meaning no such user
        else:
            return False


    def UpdateUserProfile(self, user, firstName, lastName, country, age):
        query = "UPDATE DbMysql15.DbMysql15.Users FirstName='{}', userLastName='{}', userCountry='{}', userAge={} WHERE userName='{}';".format(firstName, lastName, country, age, user)
        try:
            self.cur.execute(query)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return False

    def MakeJsonUserDetails(self,user):
        query = "SELECT * FROM DbMysql15.DbMysql15.Users WHERE DbMysql15.Users.userName='%s'"%user
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
        query = "SELECT DbMysql15.Users.userName, DbMysql15.Users.userPassword FROM DbMysql15.DbMysql15.Users WHERE DbMysql15.Users.userName='%s'"%userName
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
        query = "UPDATE DbMysql15.DbMysql15.Users SET playlistPrivacy={} WHERE userName='{}';".format(privacy, user)
        try:
            self.cur.execute(query)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return {}

    def getPlayList(self, user):
        query = "SELECT DbMysql15.Songs.trackId, DbMysql15.Songs.trackName as Song, DbMysql15.Artists.artistName AS Artist, DbMysql15.Collections.collectionName AS Album,\
		DbMysql15.TrackUser.ranking AS 'You Rated', DbMysql15.TrackUser.numberOfViews AS 'Plays',\
		DbMysql15.Songs.discNumber AS 'Disc Number', DbMysql15.Songs.trackPosition AS 'Track Position', DbMysql15.Songs.trackTimeMillis AS 'Length (msec)',\
        convert(DbMysql15.Songs.trackReleaseDate using utf8) AS 'Release Date',\
        DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS 'Price ($)', DbMysql15.Songs.previewSong\
        FROM DbMysql15.DbMysql15.Songs, DbMysql15.DbMysql15.Collections, DbMysql15.DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.DbMysql15.Artists, DbMysql15.DbMysql15.TrackUser\
        WHERE DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND\
		DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND\
        DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND\
        DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND\
        DbMysql15.TrackUser.userName = '%s' AND\
        DbMysql15.TrackUser.isInPlaylist = '1'\
        ORDER BY 4 DESC"%user
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            return False

    def AddSongToPlaylist(self, user, songId):
        query2 = "SELECT * FROM DbMysql15.DbMysql15.TrackUser where DbMysql15.TrackUser.userName = '%s' and DbMysql15.TrackUser.trackId = '%s';"%(user, songId)
        try:
            self.cur.execute(query2)
            results = self.cur.fetchall()
            if(len(results) != 0):
                query2 = "UPDATE DbMysql15.DbMysql15.TrackUser SET isInPlaylist=1 WHERE trackId='%s' and userName='%s';"%(songId, user)
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
        query2 = "INSERT INTO DbMysql15.DbMysql15.TrackUser (trackId, userName, numberOfViews, ranking, isInPlaylist)\
             VALUES ('%s', '%s', '%s', '%s', %d);"%(songId, user, 0, 0, 1)
        try:
            self.cur.execute(query2)
            self.DB.commit()
            return True
        except:
            self.DB.rollback()
            return {}

    def changeRating(self, user, rating, songId,isInPlaylist):
        query1 = "SELECT DbMysql15.TrackUser.ranking = '%s'\
        WHERE DbMysql15.TrackUser.userName = '%s' AND\
		DbMysql15.TrackUser.trackId = '%s'"%(rating, user, songId)
        try:
            self.cur.execute(query1)
            results = self.cur.fetchall()
        except:
            self.DB.rollback()
            return {}
        if(len(results) == 0):
            query2 = "INSERT INTO DbMysql15.DbMysql15.TrackUser (trackId, userName, numberOfViews, ranking, isInPlaylist)\
             VALUES ('%s', '%s', '%s', '%s', %d);"%(songId, user, 0, ranking,isInPlaylist)
            try:
                self.cur.execute(query2)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return {}
        else:
            query2 = "UPDATE DbMysql15.TrackUser SET DbMysql15.TrackUser.ranking = '%s'\
            WHERE DbMysql15.TrackUser.userName = '%s' AND\
            DbMysql15.TrackUser.trackId = '%s'"%(rating, user, songId)
            try:
                self.cur.execute(query2)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return {}

    def GetArtistTableTimeMachine(self,decadeStart,decadeEnd):
        query = """SELECT	sum(DbMysql15.TrackUser.ranking) as Rating, DbMysql15.Artists.artistName as 'Artist'
                FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Artists, DbMysql15.DbMysql15.CollectionsArtist
                WHERE	DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
		        DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY DbMysql15.Artists.artistName
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
        query = """SELECT	sum(DbMysql15.TrackUser.ranking) as Rating, DbMysql15.Songs.trackName as 'Song'
                FROM	DbMysql15.TrackUser, DbMysql15.Songs
                WHERE	DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY DbMysql15.Songs.trackName
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
	            FROM	DbMysql15.TrackUser
	            GROUP BY DbMysql15.TrackUser.trackId) as viewsPerTrack, DbMysql15.Songs 
                WHERE	viewsPerTrack.track = DbMysql15.Songs.trackId AND
		        DbMysql15.Songs.trackReleaseDate BETWEEN '{}-01-01' AND '{}-12-31'
                GROUP BY DbMysql15.Songs.trackGenre
                ORDER BY 1 DESC
                LIMIT 5""".format(decadeStart,decadeEnd)
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedDbMysql15.Songs(self,user):
        query = """SELECT	DbMysql15.Songs.trackName as Song, avg(DbMysql15.TrackUser.ranking) AS Rating, userPlaylist.numOfDbMysql15.Songs as numOfDbMysql15.Songs, DbMysql15.Collections.collectionName AS Album, DbMysql15.Artists.artistName AS Artist, DbMysql15.TrackUser.isInPlaylist,
		DbMysql15.Songs.previewSong AS Preview, DbMysql15.Songs.trackId AS 'Track ID',
		DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackReleaseDate AS 'Release Date', DbMysql15.Songs.trackPrice AS Price
FROM	(
		SELECT	DISTINCT DbMysql15.TrackUser.userName as tempUser, count(DbMysql15.TrackUser.trackId) as numOfDbMysql15.Songs, DbMysql15.Artists.artistId as artist
		FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists
		WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
				DbMysql15.TrackUser.userName = "%s" AND
				DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
		GROUP BY DbMysql15.Artists.artistId
		) AS userPlaylist, DbMysql15.Songs, DbMysql15.TrackUser, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists

WHERE	DbMysql15.Artists.artistId = userPlaylist.artist AND
		DbMysql15.TrackUser.isInPlaylist='0' AND
		userPlaylist.artist = DbMysql15.DbMysql15.CollectionsArtist.artistId AND
		DbMysql15.DbMysql15.CollectionsArtist.collectionId = DbMysql15.Collections.collectionId AND
		DbMysql15.Collections.collectionId = DbMysql15.Songs.collectionId AND
		DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId
GROUP BY DbMysql15.TrackUser.trackId
ORDER BY 2 DESC
LIMIT 100"""%user
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            print(results)
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedDbMysql15.Collections(self,user):
        query = """SELECT	DbMysql15.Collections.collectionName AS Album, DbMysql15.Collections.collectionPrice AS 'Price ($)', userPlaylist.artistName, convert(DbMysql15.Collections.collectionReleaseDate using utf8),DbMysql15.Collections.collectionGenre
FROM	(
		SELECT	DbMysql15.TrackUser.userName as tempUser, DbMysql15.TrackUser.trackId as track, DbMysql15.Artists.artistId as artistid, DbMysql15.Artists.artistName
		FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists
		WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
				DbMysql15.TrackUser.userName = "%s" AND
				DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
		) AS userPlaylist, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
WHERE	userPlaylist.artistid = DbMysql15.DbMysql15.CollectionsArtist.artistId AND
		DbMysql15.DbMysql15.CollectionsArtist.collectionId = DbMysql15.Collections.collectionId
ORDER BY 1 ASC
LIMIT 10    
                """%user
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except:
            self.DB.rollback()
            return {}

    def GetRecommendedDbMysql15.Artists(self,user):
        query = """SELECT	DbMysql15.Artists.artistName as Artist, count(userPlaylist.track) as 'Number of DbMysql15.Songs You Like of This Artist',
		        DbMysql15.Artists.artistId AS 'Artist ID'
                FROM	(
		        SELECT	DbMysql15.TrackUser.userName as tempUser, DbMysql15.TrackUser.trackId as track, DbMysql15.Artists.artistId as artist
		        FROM	DbMysql15.TrackUser, DbMysql15.Songs, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Artists
		        WHERE	DbMysql15.TrackUser.isInPlaylist = '1' AND
				DbMysql15.TrackUser.userName = "%s" AND
				DbMysql15.TrackUser.trackId = DbMysql15.Songs.trackId AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS userPlaylist, DbMysql15.Artists
                WHERE	userPlaylist.artist = DbMysql15.Artists.artistId
                GROUP BY userPlaylist.artist
                ORDER BY 2 DESC
                LIMIT 5
                """%user
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
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
            END AS ExtraParams
FROM	(SELECT  null AS Song, null AS trackId,
					null AS Album, 
                    DbMysql15.Artists.artistId as artistId,
					DbMysql15.Artists.artistName AS Artist, null AS discNumber, 
					null AS trackPosition, 
					null AS length, 
					null AS releaseDate,
					DbMysql15.Artists.artistPrimaryGenre AS Genre, null AS price,
					null AS numberOfTracks
		FROM 	DbMysql15.Artists
									 
		WHERE 	DbMysql15.Artists.artistName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)")) AS nested
UNION
SELECT  @songCurerentId:=trackId AS currentId, Song AS Song, Album AS Album, Artist AS Artist,
		discNumber AS discNumber, trackPosition AS trackPosition, length AS length,
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
            END AS ExtraParams
FROM	(SELECT  	DbMysql15.Songs.trackName AS Song, DbMysql15.Songs.trackId AS trackId,
					DbMysql15.Collections.collectionName AS Album, 
					DbMysql15.Artists.artistName AS Artist, DbMysql15.Songs.discNumber AS discNumber, 
					DbMysql15.Songs.trackPosition AS trackPosition, 
					DbMysql15.Songs.trackTimeMillis AS length, 
					DbMysql15.Songs.trackReleaseDate AS releaseDate,
					DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS price,
					null AS numberOfTracks
		FROM 		DbMysql15.Artists, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist, DbMysql15.Songs
		WHERE 	DbMysql15.Songs.trackName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)") AND
                DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS nested
UNION
SELECT 	DbMysql15.Collections.collectionId AS currentId, null AS Song, DbMysql15.Collections.collectionName AS Album, 
		DbMysql15.Artists.artistName AS Artist, null AS discNumber, 
        null AS trackPosition, 
        null AS length, 
        DbMysql15.Collections.collectionReleaseDate AS releaseDate,
        DbMysql15.Collections.collectionGenre AS genre,
        DbMysql15.Collections.collectionPrice AS price,
        DbMysql15.Collections.numberOfTracks AS numberOfTracks,
		null as ExtraParams
FROM 	DbMysql15.Artists,DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
WHERE 	DbMysql15.Collections.collectionName REGEXP Concat("([ ]|^)", @sQ,"([,. ;]|$)") AND 
		DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
        DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId;
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
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
            END AS paramsInDbMysql15.TrackUser
FROM	(SELECT  DbMysql15.Songs.trackName AS Song, DbMysql15.Songs.trackId AS trackId,
					DbMysql15.Collections.collectionName AS Album, 
					DbMysql15.Artists.artistName AS Artist, DbMysql15.Songs.discNumber AS discNumber, 
					DbMysql15.Songs.trackPosition AS trackPosition, 
					DbMysql15.Songs.trackTimeMillis AS length, 
					DbMysql15.Songs.trackReleaseDate AS releaseDate,
					DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS price,
					null AS numberOfTracks
		FROM 	DbMysql15.Songs, DbMysql15.Artists, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
									 
		WHERE 	DbMysql15.Songs.trackName REGEXP Concat("([ ]|^)", @trackName,"([,. ;]|$)") AND 
				DbMysql15.Collections.collectionName REGEXP Concat("([ ]|^)", @collectionName,"([,. ;]|$)") AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS nested
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
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
            END AS paramsInDbMysql15.TrackUser
FROM	(SELECT  DbMysql15.Songs.trackName AS Song, DbMysql15.Songs.trackId AS trackId,
					DbMysql15.Collections.collectionName AS Album, 
					DbMysql15.Artists.artistName AS Artist, DbMysql15.Songs.discNumber AS discNumber, 
					DbMysql15.Songs.trackPosition AS trackPosition, 
					DbMysql15.Songs.trackTimeMillis AS length, 
					DbMysql15.Songs.trackReleaseDate AS releaseDate,
					DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS price,
					null AS numberOfTracks
		FROM 	DbMysql15.Songs, DbMysql15.Artists, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
									 
		WHERE 	DbMysql15.Songs.trackName REGEXP Concat("([ ]|^)", @AlbumOrSong,"([,. ;]|$)") AND 
									DbMysql15.Artists.artistName REGEXP Concat("([ ]|^)", @Artist,"([,. ;]|$)")  AND 
									DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
									DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
									DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS nested
UNION
SELECT 	DbMysql15.Collections.collectionId AS currentId, null AS Song, DbMysql15.Collections.collectionName AS Album, 
		DbMysql15.Artists.artistName AS Artist, null AS discNumber, 
        null AS trackPosition, 
        null AS length, 
        DbMysql15.Collections.collectionReleaseDate AS releaseDate,
        DbMysql15.Collections.collectionGenre AS genre,
        DbMysql15.Collections.collectionPrice AS price,
        DbMysql15.Collections.numberOfTracks AS numberOfTracks,
        null as paramsInDbMysql15.TrackUser
FROM 	DbMysql15.Artists,DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
WHERE 	DbMysql15.Collections.collectionName REGEXP Concat("([ ]|^)", @AlbumOrSong,"([,. ;]|$)") AND 
		DbMysql15.Artists.artistName REGEXP Concat("([ ]|^)", @Artist,"([,. ;]|$)")  AND 
        DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
        DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId
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
        releaseDate AS releaseDate, Genre AS Genre, price AS price, numberOfTracks AS numberOfTracks,
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
            END AS paramsInDbMysql15.TrackUser
FROM	(SELECT  DbMysql15.Songs.trackName AS Song, DbMysql15.Songs.trackId AS trackId,
					DbMysql15.Collections.collectionName AS Album, 
					DbMysql15.Artists.artistName AS Artist, DbMysql15.Songs.discNumber AS discNumber, 
					DbMysql15.Songs.trackPosition AS trackPosition, 
					DbMysql15.Songs.trackTimeMillis AS length, 
					DbMysql15.Songs.trackReleaseDate AS releaseDate,
					DbMysql15.Songs.trackGenre AS Genre, DbMysql15.Songs.trackPrice AS price,
					null AS numberOfTracks
		FROM 	DbMysql15.Songs, DbMysql15.Artists, DbMysql15.Collections, DbMysql15.DbMysql15.CollectionsArtist
									 
		WHERE 	DbMysql15.Songs.trackName REGEXP Concat("([ ]|^)", @trackName,"([,. ;]|$)") AND 
				DbMysql15.Artists.artistName REGEXP Concat("([ ]|^)", @artistName,"([,. ;]|$)") AND
				DbMysql15.Collections.collectionName REGEXP Concat("([ ]|^)", @collectionName,"([,. ;]|$)") AND
				DbMysql15.Songs.collectionId = DbMysql15.Collections.collectionId AND
				DbMysql15.Collections.collectionId = DbMysql15.DbMysql15.CollectionsArtist.collectionId AND
				DbMysql15.DbMysql15.CollectionsArtist.artistId = DbMysql15.Artists.artistId) AS nested
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