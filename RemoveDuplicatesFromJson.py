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
    f = open("Tables//AlbumTable.json", "r")
    AlbumList = json.load(f)
    f.close()
    f = open("Tables//AlbumArtistTable.json", "r")
    AlbumArtistList = json.load(f)
    f.close()

    ArtistListResult = unique(ArtistList)
    AlbumListResult = unique(AlbumList)
    AlbumArtistListResult = unique(AlbumArtistList)

    f = open("Tables//ArtistsTable.json","w")
    json.dump(ArtistListResult, f)
    f.close()
    f = open("Tables//AlbumTable.json","w")
    json.dump(AlbumListResult, f)
    f.close()
    f = open("Tables//AlbumArtistTable.json","w")
    json.dump(AlbumArtistListResult, f)
    f.close()

if __name__ == "__main__":
    main()