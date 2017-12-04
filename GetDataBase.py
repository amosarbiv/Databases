import urllib.request
import json
from collections import defaultdict
"""
ArtistList = ["Talking Heads","Carl Perkins","Curtis Mayfield","R.E.M.",
              "Diana Ross and the Supremes","Lynyrd Skynyrd",
              "Nine Inch Nails","Booker T. and the MGs",
              "Guns n' Roses","Tom Petty","Carlos Santana","The Yardbirds",
              "Jay-Z","Gram Parsons","Tupac Shakur","Black Sabbath",
              "James Taylor","Eminem","Creedence Clearwater Revival",
              "The Drifters","Elvis Costello","The Four Tops",
              "The Stooges","Beastie Boys","The Shirelles","Eagles",
              "Hank Williams","Radiohead","AC/DC","Frank Zappa","The Police",
              "Jackie Wilson","The Temptations","Cream","Al Green","The Kinks",
              "Phil Spector","Tina Turner","Joni Mitchell","Metallica",
              "The Sex Pistols","Aerosmith","Parliament and Funkadelic",
              "Grateful Dead","Dr. Dre","Eric Clapton","Howlin' Wolf",
              "The Allman Brothers Band","Queen","Pink Floyd","The Band",
              "Elton John","Run-DMC","Patti Smith","Janis Joplin","The Byrds",
              "Public Enemy","Sly and the Family Stone","Van Morrison",
              "The Doors","Simon and Garfunkel","David Bowie","John Lennon",
              "Roy Orbison","Madonna","Michael Jackson","Neil Young",
              "The Everly Brothers","Smokey Robinson and the Miracles",
              "Johnny Cash","Nirvana","The Who","The Clash","Prince","The Ramones"
              "Fats Domino","Jerry Lee Lewis","Bruce Springsteen","U2","Otis Redding",
              "Bo Diddley","The Velvet Underground","Marvin Gaye","Muddy Waters",
              "Sam Cooke","Stevie Wonder","Led Zeppelin","Buddy Holly","The Beach Boys",
              "Bob Marley","Ray Charles","Aretha Franklin","Little Richard",
              "James Brown","Jimi Hendrix","Chuck Berry","The Rolling Stones",
              "Elvis Presley","Bob Dylan","The Beatles"]
"""

forbiden = ['Jackie Wilson', 'Cream', 'The Everly Brothers', 'Jimi Hendrix']


f = open("artists.json", "r")
ArtistList = json.load(f)
f.close()

def printRequestToFile(artistName):
    if ( " " in artistName ):
            artistName = artistName.replace(" ","+")
    response = urllib.request.urlopen("https://itunes.apple.com/search?term=%s&media=music&limit=100"%artistName)
    f = open("1.txt","w")
    s = str(response.read().decode('utf-8'))
    f.write(s)
    f.close()

def filterRawData(result):
    #filtering out desired paramters
    output_dict = defaultdict()
    
    for entry in result:
        
        if ( entry == "artistId" ):
            output_dict["artistId"] = result["artistId"]

        if ( entry == "artistName"):
            output_dict["artistName"] = result["artistName"]

        if ( entry == "trackId" ):
            output_dict["trackId"] = result["trackId"]
        
        if ( entry == "collectionId"):
            output_dict["collectionId"] = result["collectionId"]
        
        if ( entry == "trackName"):
            output_dict["trackName"] = result["trackName"]
        
        if ( entry == "collectionName" ):
            output_dict["collectionName"] = result["collectionName"]
        
        if ( entry == "country" ):
            output_dict["country"] = result["country"]
        
        if ( entry == "releaseDate" ):
            output_dict["releaseDate"] = result["releaseDate"]
        
        if ( entry == "primaryGenreName" ):
            output_dict["primaryGenreName"] = result["primaryGenreName"]

        if ( entry == "trackTimeMillis" ):
            output_dict["trackTimeMillis"] = result["trackTimeMillis"]
    
    return output_dict

def fixId(l, id):
    for entry in l:
        entry['artistId'] = id

def main():
    
    f = open("output_list_forbiden", "r")
    output_list = json.load(f)
    f.close()
    #output_list = list()
    counter = 162
    artistNotFound = list()
    for artist in forbiden:
        
        temp_list = list()
        artist_id = None

        print("Searching for %s"%artist)
        
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
        for result in d['results']:
            
            output_dict = filterRawData(result)

            if ( len(output_dict) > 0 ):
                """
                #getting the only artist ID
                if ((output_dict['artistName'].lower == artist.lower) and (artist_id != None)):
                    artist_id = output_dict['artistName']
                """
                temp_list.append(output_dict)
        
        fixId(temp_list, counter)
        counter+=1
        output_list+=temp_list  

                

        f.close()
    
    f = open("output_list_forbiden","w")
    json.dump(output_list, f)

    print("Artists not found:")
    print(artistNotFound)  


if __name__ == "__main__":
    f = open("output_list", "r")
    l = json.load(f)
    f.close()
    f = open("output_list_forbiden", "r")
    r = json.load(f)
    f.close()
    l += r
    f = open("output_list", "w") 
    json.dump(l, f)
    f.close()
    
