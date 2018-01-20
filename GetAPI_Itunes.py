  ####################################################################################
#           This was the first stone we laid on our project's building.              #
#     This script connects to itunes api and fetches artists, albums and songs       #
#   And writes them as one big json. it extracts data by using the artist ids as     #
# Found on artistId.json -- this file was created to contain 170 distinct artist Ids #
 ####################################################################################

import urllib.request
import json, time
from collections import defaultdict

f = open("artistID.json", "r")
ArtistList = json.load(f)
f.close()

def printRequestToFile(artist):
    response = urllib.request.urlopen("https://itunes.apple.com/lookup?id=%s&entity=album&limit=100"%artist["artistId"])
    f = open("1.txt","w")
    s = response.read().decode('utf-8').encode('ascii','ignore')
    s = s.decode('utf-8')
    f.write(s)
    f.close()

def filterRawData(artistWrapper, collectionWrapper):
    #filtering out desired paramters
    outputlist = []
    if(collectionWrapper["collectionType"]!="Album"):
        return []

    try:
        albumlink = "https://itunes.apple.com/lookup?id=%s&entity=song"%collectionWrapper["collectionId"]
        response = urllib.request.urlopen(albumlink)
        f = open("2.txt","w")
        s = response.read().decode('utf-8').encode('ascii','ignore')
        s = s.decode('utf-8')
        f.write(s)
        f.close()
        f = open("2.txt", "r")
        tracks = json.load(f)
        f.close()
    except:
        print("Missed")
        return []

    tracks = tracks["results"]

    for i in range(1,len(tracks)):
        try:
            output_dict = defaultdict()
            output_dict["trackId"] = tracks[i]["trackId"]
            output_dict["trackName"] = tracks[i]["trackName"]
            output_dict["collectionName"] = collectionWrapper["collectionName"]
            output_dict["artistId"] = artistWrapper["artistId"]
            output_dict["artistName"] = artistWrapper["artistName"]
            output_dict["collectionId"] = collectionWrapper["collectionId"]
            output_dict["trackTimeMillis"] = tracks[i]["trackTimeMillis"]
            output_dict["trackPosition"] = tracks[i]["trackNumber"]
            output_dict["discNumber"] =  tracks[i]["discNumber"]
            output_dict["numberOfTracks"] = collectionWrapper["trackCount"]
            output_dict["albumReleaseDate"] = collectionWrapper["releaseDate"]
            output_dict["trackReleaseDate"] = tracks[i]["releaseDate"]
            output_dict["trackPrice"] = tracks[i]["trackPrice"]
            output_dict["collectionPrice"] = collectionWrapper["collectionPrice"]
            output_dict["artistPrimaryGenreName"] = artistWrapper["primaryGenreName"]
            output_dict["albumPrimaryGenreName"] = collectionWrapper["primaryGenreName"]
            output_dict["currency"] = collectionWrapper["currency"]
            output_dict["country"] = collectionWrapper["country"]
            outputlist.append(output_dict)
        except:
            continue
    return outputlist

def fixId(l, id):
    for entry in l:
        entry['artistId'] = id

def main():
    output_list = list()
    counter = 0
    artistNotFound = list()
    for artist in ArtistList:

        temp_list = list()
        artist_id = None

        print("Searching for %s"%artist["artistName"])
        
        try:
            printRequestToFile(artist)
            #convert file to dictionary
            f = open("1.txt", "r")
            d = json.load(f)
        except Exception as e:
            artistNotFound.append(artist)
            print(str(e))
            continue

        output_dict = defaultdict()

        resultsCollection = d["results"]
        artistWrapper = resultsCollection[0]
        for i in range(1,len(resultsCollection)):
            
            outputList = filterRawData(artistWrapper, resultsCollection[i])
            if(len(outputList) > 0):
                temp_list+=outputList
        
        fixId(temp_list, counter)
        counter+=1
        output_list+=temp_list
        f.close()
    
    f = open("output_list","a")
    json.dump(output_list, f)

    print("Artists not found:")
    print(artistNotFound)  


if __name__ == "__main__":
    main()
