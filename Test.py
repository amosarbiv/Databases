import json
from collections import defaultdict
from random import randint

def main():
    f = open("SongsId.json","r")
    songsId = json.load(f)
    f.close()
    f = open("Tables//UsersTable.json","r")
    users = json.load(f)
    f.close()

    views = []
    ranks = []
    
    for user in users:
        for i in range(0,20):
            viewDic = {}
            rankDic = {}
            viewDic["UserId"] = user["UserId"]
            rankDic["UserId"] = user["UserId"]
            viewNum = randint(0, 20)
            songIdRand = randint(0, len(songsId)-1)
            rank = randint(0, 10)
            viewDic["SongId"] = songsId[songIdRand]
            rankDic["SongId"] = songsId[songIdRand]
            viewDic["Views"] = viewNum
            rankDic["Ranking"] = rank
            views.append(viewDic)
            ranks.append(rankDic)

    f = open("Tables//Views.json","w")
    json.dump(views, f)
    f.close()
    f = open("Tables//Rankings.json","w")
    json.dump(ranks, f)
    f.close()


if __name__ == "__main__":
    main()