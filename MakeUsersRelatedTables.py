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
        for i in range(0,length):
            s = set()
            trackUserDic = {}
            
            isInPlaylist = randint(0,1)

            if(isInPlaylist == 1):
                viewNum = randint(1, 20)
            else:
                viewNum = randint(0, 20)
            
            songIdRand = randint(0, len(songsId)-1)
            while(songIdRand in s):
                songIdRand = randint(0, len(songsId)-1)
            s.add(songIdRand)
            rankTrack = randint(1, 10)
            

            trackUserDic["trackId"] = songsId[songIdRand]["trackId"]
            trackUserDic["userName"] = user["userName"]
            trackUserDic["numberOfViews"] = viewNum
            trackUserDic["trackRank"] = rankTrack
            trackUserDic["isInPlaylist"] = isInPlaylist

            trackUser.append(trackUserDic)


            
            rankArtists = randint(1, 10)
            for i in range(0,rankArtists):
                artistRankingDic = {}
                randArtist = randint(0, len(artists)-1)
                rank = randint(1, 10)
                artistRankingDic["userName"] = user["userName"]
                artistRankingDic["artistId"] = artists[randArtist]["artistId"]
                artistRankingDic["artistRanking"] = rank
                artistRanking.append(artistRankingDic)
        counter += 1


    f = open("Tables//ArtistRankingTable.json","w")
    json.dump(artistRanking, f)
    f.close()
    f = open("Tables//TrackUserTable.json","w")
    json.dump(trackUser, f)
    f.close()


if __name__ == "__main__":
    main()