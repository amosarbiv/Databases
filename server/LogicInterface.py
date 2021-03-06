 #############################################################################
#       This script recieves request through  server, it figures the right    #             #
# Query and format that needed to be activated, and activate them using DBapi #
 #############################################################################

import pymysql as sql
import logging
import os
import json
import DBapi
import decimal

absPath = os.path.dirname(__file__) #<-- absolute dir the script is in

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
        rel_path = 'tmpFiles/userProfile.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
        details = json.load(f)
        f.close()
        return json.dumps(details)

    def UpdateUserProfile(self,firstName,lastName,country,age):
        rel_path = 'tmpFiles/userProfile.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
        profile = json.load(f)
        f.close()
        currUserName = profile['UserName']
        password = profile['Password']
        self.dataBase.UpdateUserProfile(currUserName,firstName,lastName,country,age)
        newDic = {"UserName":currUserName,"Password":password,"FirstName":firstName,"LastName":lastName,"Country":country,"Age":age,"PlaylistPrivacy":profile['PlaylistPrivacy']}
        f = open(fullPath, "w")
        json.dump(newDic, f)
        f.close() 
        return currUserName

    def MakeUserProfileJson(self, user):
        self.dataBase.MakeJsonUserDetails(user)

    def ChangePlaylistPrivacy(self, privacy):
        rel_path = 'tmpFiles/userProfile.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
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
        f = open(fullPath, "w")
        json.dump(profile, f)
        f.close() 
        return result

    def displayPlayList(self, user):
        playList = self.dataBase.getPlayList(user)
        if (not playList):
            return ""
        else:
            return playList

    def playlistChangeRating(self, user, rating, typeId, typeString, isInPlaylist):
        if(typeString == 'starsSong'):
            self.dataBase.changeTrackRating(user, rating, typeId, isInPlaylist)
        else:
            self.dataBase.changeArtistRating(user, rating, typeId)
        return

    def AddSongToPlaylist(self, user, songId):
        self.dataBase.AddSongToPlaylist(user, songId)
        return

    def GetTableTimeMachine(self):
        rel_path = 'tmpFiles/userSearchTerm.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
        args = json.load(f)
        f.close()
        typeTimeMachine = args["Type"]
        decade = args["Decade"]
        if(decade == "50's"):
            decadeStart = 1950
            decadeEnd = 1959
        elif(decade == "60's"):
            decadeStart = 1960
            decadeEnd = 1969
        elif(decade == "70's"):
            decadeStart = 1970
            decadeEnd = 1979
        elif(decade == "80's"):
            decadeStart = 1980
            decadeEnd = 1989
        elif(decade == "90's"):
            decadeStart = 1990
            decadeEnd = 1999
        elif(decade == "2000's"):
            decadeStart = 2000
            decadeEnd = 2009
        if(typeTimeMachine == "Artist"):
            result = self.dataBase.GetArtistTableTimeMachine(decadeStart,decadeEnd)
        if(typeTimeMachine == "Song"):
            result = self.dataBase.GetSongTableTimeMachine(decadeStart,decadeEnd)
        if(typeTimeMachine == "Genre"):
            result = self.dataBase.GetGenreTableTimeMachine(decadeStart,decadeEnd)
        finalList=[]
        for row in result:
            rowDic = {}
            col1 = row[0]
            col2 = row[1]
            if (isinstance(col1, decimal.Decimal)):
                col1 = float(row[0])
            if (isinstance(col2, decimal.Decimal)):
                col2 = float(row[1])
            rowDic['col1'] = col1
            rowDic['col2'] = col2
            finalList.append(rowDic)
        return finalList

    def GetTableTrending(self):
        rel_path = 'tmpFiles/userSearchTerm.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
        args = json.load(f)
        f.close()
        typeTrending = args["Type"]
        TypeOfSearch = args["TypeOfSearch"]
        if(typeTrending == "Artist"):
            indexTypeOfSearch = 0
            if(TypeOfSearch == "Top 20"):
                indexTypeOfSearch = 0
            elif(TypeOfSearch == "Top 10 by girls"):
                indexTypeOfSearch = 1
            elif(TypeOfSearch == "Top 10 by guys"):
                indexTypeOfSearch = 2
            elif(TypeOfSearch == "Top 5 in pop"):
                indexTypeOfSearch = 3
            elif(TypeOfSearch == "Top 5 in rock"):
                indexTypeOfSearch = 4
            result = self.dataBase.GetArtistTableTrending(indexTypeOfSearch)
        elif(typeTrending == "Songs"):
            indexTypeOfSearch = 0
            if(TypeOfSearch == "Top 25"):
                indexTypeOfSearch = 0
            elif(TypeOfSearch == "Top 10 by girls"):
                indexTypeOfSearch = 1
            elif(TypeOfSearch == "Top 10 by guys"):
                indexTypeOfSearch = 2
            elif(TypeOfSearch == "Top 10 by people > 50"):
                indexTypeOfSearch = 3
            elif(TypeOfSearch == "Top 10 by people 30-50"):
                indexTypeOfSearch = 4
            elif(TypeOfSearch == "Top 10 by people < 30"):
                indexTypeOfSearch = 5
            result = self.dataBase.GetSongTableTrending(indexTypeOfSearch)
        elif(typeTrending == "Collection"):
            indexTypeOfSearch = 0
            if(TypeOfSearch == "Top 10"):
                indexTypeOfSearch = 0
            elif(TypeOfSearch == "Top 10 by girls"):
                indexTypeOfSearch = 1
            elif(TypeOfSearch == "Top 10 by guys"):
                indexTypeOfSearch = 2
            elif(TypeOfSearch == "Top 5 in pop"):
                indexTypeOfSearch = 3
            elif(TypeOfSearch == "Top 5 in rock"):
                indexTypeOfSearch = 4
            result = self.dataBase.GetCollectionTableTrending(indexTypeOfSearch)
        finalList=[]
        for row in result:
            rowDic = {}
            col1 = row[0]
            col2 = row[1]
            if (isinstance(col1, decimal.Decimal)):
                col1 = float(row[0])
            if (isinstance(col2, decimal.Decimal)):
                col2 = float(row[1])
            rowDic['col1'] = col1
            rowDic['col2'] = col2
            finalList.append(rowDic)
        return finalList

    def GetUserSearchTerm(self, arg):
        rel_path = 'tmpFiles/userSearchTerm.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "w")
        json.dump(arg, f)
        f.close()

    def GetRecommendedData(self):
        currUserName = self.GetUserName()
        songsTable = self.dataBase.GetRecommendedSongs(currUserName)
        artistsTable = self.dataBase.GetRecommendedArtists(currUserName)
        collectionsTable = self.dataBase.GetRecommendedCollections(currUserName)
        recommendedTable = {}
        recommendedTable['songs'] = songsTable
        recommendedTable['artists'] = artistsTable
        recommendedTable['collections'] = collectionsTable
        return recommendedTable

    def GetUserName(self):
        rel_path = 'tmpFiles/userProfile.json'
        fullPath = os.path.join(absPath, rel_path)
        f = open(fullPath, "r")
        profile = json.load(f)
        f.close()
        return profile['UserName']

    def RetrieveSearchInfo(self, userName, searchTerm):
        if((searchTerm.find(';') != -1) or (searchTerm.find('"') != -1)):
            return False
        if(searchTerm.find('<') == -1 and searchTerm.find('>') == -1):
            result = self.dataBase.RetrieveAllTypes(userName, searchTerm)
            resultAVG = self.dataBase.GetAverageRating()
            result = self.PrepareDictionary(result, resultAVG)   
            return result
        
        song=""
        album=""
        artist=""
        songInd = False
        albumInd = False
        artistInd = False
        byInd = False
        inInd = False
        inPhrase = False
        betweenConnector = ""
        for ch in searchTerm:
            if(ch == '<'):
                if(song != "" and album != "" and artist != ""):
                    return False
                if(inPhrase == False and betweenConnector == "" and (song != "" or album != "")):
                    return False
                if(inPhrase == False and betweenConnector != ""):
                    if(betweenConnector == "in"):
                        inInd = True
                    elif(betweenConnector == "by"):
                        byInd = True
                    else:
                        return False
                    betweenConnector = ""
                inPhrase = True
                if(song == ""):
                    songInd = True
                elif((song != "") and (inInd == True) and (album == "")):
                    albumInd = True
                elif((song != "") and (byInd == True) and (artist == "")):
                    artistInd = True
            elif(ch == '>'):
                if(inPhrase == False):
                    return False
                if(song != ""):
                    songInd = False
                if(album != ""):
                    albumInd = False
                if(artist != ""):
                    artistInd = False
                inPhrase = False
            elif(songInd==True):
                song += ch
            elif(albumInd == True):
                album += ch
            elif(artistInd == True):
                artist += ch
            else:
                if(song == "" and album == "" and artist == ""):
                    return False
                if(ch != " "):
                    betweenConnector += ch

        if(betweenConnector != "" or inPhrase == True):
            return False
        
        result = []
        if(song != "" and album == "" and artist == ""):
            result = self.dataBase.RetrieveAllTypes(userName, song)
        elif(song != "" and album != "" and artist == "" and inInd == True and byInd == False):
            result = self.dataBase.RetrieveSongAlbum(userName, song, album)
        elif(song != "" and album == "" and artist != "" and inInd == False and byInd == True):
            result = self.dataBase.RetrieveSongORAlbumArtist(userName, song, artist)
        elif(song != "" and album != "" and artist != "" and inInd == True and byInd == True):
            result = self.dataBase.RetrieveSongAlbumArtist(userName, song, album, artist)

        resultAVG = self.dataBase.GetAverageRating()
        result = self.PrepareDictionary(result, resultAVG)   
        return result

    def PrepareDictionary(self, table, resultAVG):
        avgDic = {}
        for i in range(0,len(resultAVG)):
            avgDic[resultAVG[i][0]] = resultAVG[i]

        result = {}
        songList = []
        artistList = []
        collectionList = []
        for i in range(0, len(table)):
            tmpDic = {}
            row = table[i]
            currId = row[0]
            song = row[1]
            album = row[2]
            artist = row[3]
            discNumber = row[4]
            trackPosition = row[5]
            length = row[6]
            genre = row[7]
            price = row[8]
            previewSong = row[9]
            numOfTracks = row[10]
            extraParams = row[11]
            if(song != None):
                tmpDic['id'] = currId
                tmpDic['song'] = song
                tmpDic['album'] = album
                tmpDic['artist'] = artist
                tmpDic['discNumber'] = discNumber
                tmpDic['trackPosition'] = trackPosition
                tmpDic['length'] = length
                tmpDic['genre'] = genre
                tmpDic['price'] = price
                tmpDic['previewSong'] = previewSong
                if (extraParams != None):
                    tmpDic['extraParams'] = extraParams
                else:
                    tmpDic['extraParams'] = -1
                if(currId in avgDic):
                    tmpDic['rating'] = avgDic[currId][1]
                else:
                    tmpDic['rating'] = 0
                songList.append(tmpDic)
            elif(album != None):
                tmpDic['id'] = currId
                tmpDic['album'] = album
                tmpDic['artist'] = artist
                tmpDic['genre'] = genre
                tmpDic['price'] = price
                tmpDic['numOfTracks'] = numOfTracks
                collectionList.append(tmpDic)
            else:
                tmpDic['id'] = currId
                tmpDic['artist'] = artist
                tmpDic['genre'] = genre
                if (extraParams != None):
                    tmpDic['extraParams'] = extraParams
                else:
                    tmpDic['extraParams'] = -1
                artistList.append(tmpDic)
        result['songs'] = songList
        result['album'] = collectionList
        result['artist'] = artistList
        return result

    def GetSongAttributes(self, user, songId):
        return self.dataBase.GetSongAttributes(user, songId)

    def UpdateNumOfPlays(self,userName,trackId,numOfPlays):
        self.dataBase.UpdateNumOfPlays(userName,trackId,numOfPlays)

    def RetrieveAlbumsFromArtist(self,userName,artistId):
        return self.dataBase.RetrieveAlbumsFromArtist(userName,artistId)

    
