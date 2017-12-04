import json

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



def compare(l):
    for artist in ArtistList:
        if artist not in l:
            print("%s not in our list"%artist)

def main():
    f = open("output_list", "r")
    output = list()
    l = json.load(f)
    for i in l:
        for entry in i:
            if (entry == "artistName"):
                if ( i["artistName"] not in output ):
                    output.append(i["artistName"])
    

    compare(output)



if __name__ == "__main__":
    main()