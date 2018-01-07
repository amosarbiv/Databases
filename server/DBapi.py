import MySQLdb as sql
import logging
import os
import json

ArtistSearch = "SELECT	artists.artistName AS Artist, artists.artistPrimaryGenre AS Genre FROM	artists, artistuser   WHERE	artistuser.artistId = artists.artistId AND LOWER(artists.artistName) LIKE LOWER('%{}%') GROUP BY artists.artistName"
SongSearch = """SELECT Songs.trackName as Song, Artists.artistName AS Artist, Collections.collectionName AS Album,
		Songs.discNumber AS 'Disc Number', Songs.trackPosition AS 'Track Position', Songs.trackTimeMillis AS 'Length (msec)',
        Songs.trackReleaseDate AS 'Release Date',
        Songs.trackGenre AS Genre, Songs.trackPrice AS 'Price ($)'
        FROM	Songs, Collections, collectionsartist, Artists	
        WHERE	Songs.collectionId = collections.collectionId AND
		collections.collectionId = collectionsartist.collectionId AND
        collectionsartist.artistId = Artists.artistId AND
        LOWER(Songs.trackName) LIKE LOWER('{}')
        ORDER BY 2 ASC;"""
CollectionSearch = """ SELECT	collections.collectionName AS Album, Artists.artistName AS Artist,
        collections.numberOfTracks AS 'Number of Tracks',
        collections.collectionGenre AS Genre, Collections.collectionPrice AS 'Price ($)',
        Collections.country AS 'Country of Origin', collections.collectionReleaseDate AS 'Release Date'
        FROM	collections, collectionsartist, artists
        WHERE	collections.collectionId = collectionsartist.collectionId AND
		collectionsartist.artistId = artists.artistId AND
        LOWER(collections.collectionName) LIKE LOWER('{}')
        GROUP BY 2"""

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
            print("commited")
            return True
        except:
            self.DB.rollback()
            return False  
