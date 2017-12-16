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

    views = []
    ranks = []
    playlistUser = []
    playlist = []
    counter = 0
    
    for user in users:
        playlistUserDic = {}
        playlistUserDic["userId"] = user["userId"]
        playlistUserDic["playlistId"] = counter
        playlistUser.append(playlistUserDic)
        length = randint(10, 20)
        for i in range(0,length):
            s = set()
            viewDic = {}
            rankDic = {}
            playlistDic = {}
            playlistDic["userId"] = user["userId"]
            viewDic["userId"] = user["userId"]
            rankDic["userId"] = user["userId"]
            viewNum = randint(0, 20)
            songIdRand = randint(0, len(songsId)-1)
            while(songIdRand in s):
                songIdRand = randint(0, len(songsId)-1)
            s.add(songIdRand)
            rank = randint(0, 10)
            publicPrivate = randint(0, 1)
            playlistDic["playlistId"] = counter
            playlistDic["trackId"] = songsId[songIdRand]["trackId"]
            if(publicPrivate == 0):
                playlistDic["privacy"] = "public"
            else:
                playlistDic["privacy"] = "private"
            viewDic["trackId"] = songsId[songIdRand]["trackId"]
            rankDic["trackId"] = songsId[songIdRand]["trackId"]
            viewDic["views"] = viewNum
            rankDic["ranking"] = rank
            views.append(viewDic)
            ranks.append(rankDic)
            playlist.append(playlistDic)
        counter += 1

    f = open("Tables//Views.json","w")
    json.dump(views, f)
    f.close()
    f = open("Tables//Rankings.json","w")
    json.dump(ranks, f)
    f.close()
    f = open("Tables//UserPlaylists.json","w")
    json.dump(playlistUser, f)
    f.close()
    f = open("Tables//Playlists.json","w")
    json.dump(playlist, f)
    f.close()


if __name__ == "__main__":
    main()