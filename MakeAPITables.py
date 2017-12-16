import json
from collections import defaultdict

def main():
    
    f = open("output_list", "r")
    dataBase = json.load(f)
    f.close()

    songsTable = list()
    albumTable = list()
    albumSongTable = list()
    artistsTable = list()
    artistSongTable = list()
    albumArtistTable = list()

    for  dictionary in dataBase:

        #Songs Dictionary
        songsDict = defaultdict()
        songsDict["trackId"] = dictionary["trackId"]
        songsDict["trackName"] = dictionary["trackName"]
        songsDict["trackPrice"] = dictionary["trackPrice"]
        songsDict["trackTimeMillis"] = dictionary["trackTimeMillis"]
        songsDict["TrackGenre"] = dictionary["albumPrimaryGenreName"]
        songsDict["trackReleaseDate"] = dictionary["trackReleaseDate"]
        songsDict["country"] = dictionary["country"]
        songsTable.append(songsDict)

        #Album Dictionary
        albumDict = defaultdict()
        albumDict["collectionId"] = dictionary["collectionId"]
        albumDict["collectionName"] = dictionary["collectionName"]
        albumDict["numberOfTracks"] = dictionary["numberOfTracks"]
        albumDict["collectionReleaseDate"] = dictionary["albumReleaseDate"]
        albumDict["collectionPrice"] = dictionary["collectionPrice"]
        albumDict["collectionGenre"] = dictionary["albumPrimaryGenreName"]
        albumDict["collectionGenre"] = dictionary["albumPrimaryGenreName"]
        albumDict["country"] = dictionary["country"]
        albumTable.append(albumDict)

        #Artist Dictionary
        artistDict = defaultdict()
        artistDict["artistId"] = dictionary["artistId"]
        artistDict["artistName"] = dictionary["artistName"]
        artistDict["artistPrimaryGenre"] = dictionary["artistPrimaryGenreName"]
        artistsTable.append(artistDict)

        #Artist Song Dictionary
        artistSongDict = defaultdict()
        artistSongDict["trackId"] = dictionary["trackId"]
        artistSongDict["artistId"] = dictionary["artistId"]
        artistSongTable.append(artistSongDict)

        #Album Artist Dictionary
        albumArtistDict = defaultdict()
        albumArtistDict["collectionId"] = dictionary["collectionId"]
        albumArtistDict["artistId"] = dictionary["artistId"]
        albumArtistTable.append(albumArtistDict)

        #Album Song Dictionary
        albumSongDict = defaultdict()
        albumSongDict["trackId"] = dictionary["trackId"]   
        albumSongDict["collectionId"] = dictionary["collectionId"]
        albumSongDict["trackPosition"] = dictionary["trackPosition"]
        albumSongDict["discNumber"] = dictionary["discNumber"]
        albumSongTable.append(albumSongDict)
        
    f = open("Tables//SongsTable.json","w")
    json.dump(songsTable, f)
    f.close()

    f = open("Tables//AlbumTable.json","w")
    json.dump(albumTable, f)
    f.close()

    f = open("Tables//AlbumSongsTable.json","w")
    json.dump(albumSongTable, f)
    f.close()

    f = open("Tables//ArtistsTable.json","w")
    json.dump(artistsTable, f)
    f.close()

    f = open("Tables//ArtistSongTable.json", "w")
    json.dump(artistSongTable, f)
    f.close()

    f = open("Tables//AlbumArtistTable.json","w")
    json.dump(albumArtistTable, f)
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
