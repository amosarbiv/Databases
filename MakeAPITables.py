import json
from collections import defaultdict

def main():
    
    f = open("output_list", "r")
    dataBase = json.load(f)
    f.close()

    artistsTable = list()
    songsTable = list()
    collectionTable = list()

    for  dictionary in dataBase:

        #Songs Dictionary
        songsDict = defaultdict()
        songsDict["trackId"] = dictionary["trackId"]
        songsDict["trackName"] = dictionary["trackName"]
        songsDict["collectionId"] = dictionary["collectionId"]
        songsDict["discNumber"] = dictionary["discNumber"]
        songsDict["trackPosition"] = dictionary["trackPosition"]
        songsDict["trackReleaseDate"] = dictionary["trackReleaseDate"]
        songsDict["trackTimeMillis"] = dictionary["trackTimeMillis"]
        songsDict["trackGenre"] = dictionary["albumPrimaryGenreName"]
        songsDict["trackPrice"] = dictionary["trackPrice"]
        songsTable.append(songsDict)

        #Album Dictionary
        albumDict = defaultdict()
        albumDict["collectionId"] = dictionary["collectionId"]
        albumDict["artistId"] = dictionary["artistId"]
        albumDict["collectionName"] = dictionary["collectionName"]
        albumDict["collectionReleaseDate"] = dictionary["albumReleaseDate"]
        albumDict["collectionPrice"] = dictionary["collectionPrice"]
        albumDict["country"] = dictionary["country"]
        albumDict["collectionGenre"] = dictionary["albumPrimaryGenreName"]
        albumDict["numberOfTracks"] = dictionary["numberOfTracks"]
        collectionTable.append(albumDict)

        #Artist Dictionary
        artistDict = defaultdict()
        artistDict["artistId"] = dictionary["artistId"]
        artistDict["artistName"] = dictionary["artistName"]
        artistDict["artistPrimaryGenre"] = dictionary["artistPrimaryGenreName"]
        artistsTable.append(artistDict)
        
    f = open("Tables//SongsTable.json","w")
    json.dump(songsTable, f)
    f.close()

    f = open("Tables//CollectionTable.json","w")
    json.dump(collectionTable, f)
    f.close() 

    f = open("Tables//ArtistsTable.json","w")
    json.dump(artistsTable, f)
    f.close() 


def removeduplicate(it):
    seen = set()
    for x in it:
        t = tuple(x.items())
        if t not in seen:
            yield x
            seen.add(t)      
        
if __name__ == "__main__":
    main()
