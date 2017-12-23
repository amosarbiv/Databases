import urllib.request
import json, time
from collections import defaultdict

def unique(sequence):
    seen = set()
    new_l = []
    for d in sequence:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l

def main():
    f = open("Tables//ArtistsTable.json", "r")
    ArtistList = json.load(f)
    f.close()
    f = open("Tables//CollectionTable.json", "r")
    AlbumList = json.load(f)
    f.close()

    ArtistListResult = unique(ArtistList)
    AlbumListResult = unique(AlbumList)

    f = open("Tables//ArtistsTable.json","w")
    json.dump(ArtistListResult, f)
    f.close()
    f = open("Tables//CollectionTable.json","w")
    json.dump(AlbumListResult, f)
    f.close()

if __name__ == "__main__":
    main()