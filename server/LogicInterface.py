import MySQLdb as sql
import logging
import os
import json
import DBapi

class LogicInter:

    def __init__(self, DBUserName, DBPasswd, DBName):
        self.dataBase = DBapi.DB(DBUserName, DBPasswd, DBName)

    def HandleLoginAction(self,chkBox,user,password):
        return self.dataBase.CheckUserLogin(user, password)

    def HandleUserCreation(self, user, password, firstName, lastName, age, country, radioGender):
        if(radioGender == "Male"):
            radioGender = "M"
        if(radioGender == "Female"):
            radioGender = "F"
        else:
            radioGender = "N"
        return self.dataBase.CreateUser(user, password, firstName, lastName, age, country, radioGender)

    def GetUserProfile(self):
        f = open("server//tmpFiles//userProfile.json", "r")
        details = json.load(f)
        f.close()
        return json.dumps(details)

    def UpdateUserProfile(self,password,firstName,lastName,country,age):
        f = open("server//tmpFiles//userProfile.json", "r")
        profile = json.load(f)
        f.close()
        currUserName = profile['UserName']
        self.dataBase.UpdateUserProfile(currUserName,password,firstName,lastName,country,age)
        newDic = {"UserName":currUserName,"Password":password,"FirstName":firstName,"LastName":lastName,"Country":country,"Age":age,"PlaylistPrivacy":profile['PlaylistPrivacy']}
        f = open("server//tmpFiles//userProfile.json","w")
        json.dump(newDic, f)
        f.close() 
        return currUserName

    def MakeUserProfileJson(self, user):
        self.dataBase.MakeJsonUserDetails(user)

    def ChangePlaylistPrivacy(self, privacy):
        f = open("server//tmpFiles//userProfile.json", "r")
        profile = json.load(f)
        f.close()
        currUserName = profile['UserName']
        if(privacy == True): 
            privacy = 1
            profile['PlaylistPrivacy'] = 1
        else: 
            privacy = 0
            profile['PlaylistPrivacy'] = 0
        result = self.dataBase.UpdatePrivacy(privacy, currUserName)
        f = open("server//tmpFiles//userProfile.json","w")
        json.dump(profile, f)
        f.close() 
        return result

    def displayPlayList(self, user):
        playList = self.dataBase.getPlayList(user)
        if (not playList):
            return ""
        else:
            return playList


    