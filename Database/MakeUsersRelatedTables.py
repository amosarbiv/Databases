 #####################################################################################
#                   This script connects users to artists & songs by                  #
# Creating trackUser json that contains all tracks user has viewed/ranked/in playlist #      #
 ####################################################################################

import json
from collections import defaultdict
from random import randint

def main():
    f = open("Tables//SongsTable.json","r")
    songsId = json.load(f)
    f.close()
    f = open("Tables//UsersTable.json","r")
    users = json.load(f)
    f.close()
    f = open("Tables//ArtistsTable.json","r")
    artists = json.load(f)
    f.close()

    trackUser = []
    artistRanking = []
    counter = 0
    
    for user in users:
        length = randint(20, 30)
        s = set()
        for i in range(0,length):
            trackUserDic = {}
            
            isInPlaylist = randint(0,1)

            viewNum = randint(1, 20)
            
            songIdRand = randint(0, len(songsId)-1)
            while(songIdRand in s):
                songIdRand = randint(0, len(songsId)-1)
            s.add(songIdRand)
            rankTrack = randint(1, 5)
            

            trackUserDic["trackId"] = songsId[songIdRand]["trackId"]
            trackUserDic["userName"] = user["userName"]
            trackUserDic["numberOfViews"] = viewNum
            trackUserDic["ranking"] = rankTrack
            trackUserDic["isInPlaylist"] = isInPlaylist
            trackUser.append(trackUserDic)
            
            rankArtists = randint(1, 10)
            s1 = set()
            for i in range(0,rankArtists):
                artistRankingDic = {}
                randArtist = randint(0, len(artists)-1)
                while(randArtist in s1):
                    randArtist = randint(0, len(artists)-1)
                s1.add(randArtist)
                
                rank = randint(1, 5)
                artistRankingDic["userName"] = user["userName"]
                artistRankingDic["artistId"] = artists[randArtist]["artistId"]
                artistRankingDic["artistRanking"] = rank
                artistRanking.append(artistRankingDic)
        counter += 1


    f = open("Tables//ArtistUserTable.json","w")
    json.dump(artistRanking, f)
    f.close()
    f = open("Tables//TrackUserTable.json","w")
    json.dump(trackUser, f)
    f.close()


if __name__ == "__main__":
    main()
