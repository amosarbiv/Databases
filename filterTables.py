import json

Tables = ["AlbumArtistTable.json", "AlbumSongsTable.json", "AlbumTable.json", "ArtistsTable.json", "SongsTable.json"]


def main(): 
    for table in Tables:
        outputList = list()
        f = open(table,"r")
        toFilter =  json.load(f)
        f.close()
        for entry in toFilter:
            if (entry not in outputList):
                outputList.append(entry)
        f = open(table,"w")
        json.dump(outputList, f)
        f.close()

if __name__ == "__main__":
    main()