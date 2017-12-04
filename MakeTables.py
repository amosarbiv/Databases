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

        artistSongDict = defaultdict()
        albumArtistDict = defaultdict()
        artistDict = defaultdict()
        songsDict = defaultdict()
        albumDict = defaultdict()
        albumSongDict = defaultdict()
        
        for  entry in dictionary :
            
            if ( entry == "trackId" ):
                songsDict["trackId"] = dictionary["trackId"]
                albumSongDict["trackId"] = dictionary["trackId"]
                artistSongDict["trackId"] = dictionary["trackId"]
            
            if ( entry == "artistName" ):
                artistDict["artistName"] = dictionary["artistName"]

            if ( entry == "trackName"):
                songsDict["trackName"] = dictionary["trackName"]
            
            if ( entry == "primaryGenreName"):
                songsDict["primaryGenreName"] = dictionary["primaryGenreName"]
            
            if ( entry == ["country"] ):
                artistDict["country"] = dictionary["country"]
            
            if ( entry == "collectionName" ):
                albumDict["collectionName"] = dictionary["collectionName"]
            
            if ( entry == "releaseDate"):
                #albumDict["releaseDate"] = dictionary["releaseDate"]
                songsDict["releaseDate"] = dictionary["releaseDate"]

            if ( entry == "collectionId" ):
                albumDict["collectionId"] = dictionary["collectionId"]
                albumSongDict["collectionId"] = dictionary["collectionId"]
                albumArtistDict["collectionId"] = dictionary["collectionId"]
            
            if ( entry == "artistId"):
                artistSongDict["artistId"] = dictionary["artistId"]
                artistDict["artistId"] = dictionary["artistId"]
                albumArtistDict["artistId"] = dictionary["artistId"]
            
            if ( entry == "trackName" ):
                songsDict["trackName"] = dictionary["trackName"]

            if ( entry == "trackTimeMillis" ):
                songsDict["trackTimeMillis"] = dictionary["trackTimeMillis"]

        artistSongTable.append(artistSongDict)
        songsTable.append(songsDict)
        albumTable.append(albumDict)
        albumSongTable.append(albumSongDict)
        artistsTable.append(artistDict)
        albumArtistTable.append(albumArtistDict)

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

    f = open("AlbumArtistTable.json","w")
    json.dump(albumArtistTable, f)
    f.close()    

            
        
if __name__ == "__main__":
    main()