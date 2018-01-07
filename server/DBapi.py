import MySQLdb as sql
import logging
import os
import json

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
        self.cur.execute(query)
        results = self.cur.fetchall()
        (userName, password,firstName,lastName,country,gender,age,privacy) = results[0]
        if((privacy and 1) == 1): privacy=1
        else: privacy = 0
        dic = {"UserName":userName,"Password":password,"FirstName":firstName,"LastName":lastName,"Country":country,"Age":age,"PlaylistPrivacy":privacy}
        f = open("server//tmpFiles//userProfile.json","w")
        json.dump(dic, f)
        f.close() 

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
            return False  

    def getPlayList(self, user):
        query = "Select * FROM test.artists"
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            print(type(results))
            return results
        except:
            return False