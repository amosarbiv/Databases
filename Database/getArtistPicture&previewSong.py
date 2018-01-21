  ##########################################################################
# After building the database we decided to make our site even better..    #
# We are now supporting Artists images & playing preview of each song in   # 
# The system. The new fields are varchar and will contain the relevant url #
 ##########################################################################

import MySQLdb as sql
import logging
import os
import json

def main():
    DB = sql.connect(host="localhost",
                        user="DbMysql15",
                        passwd="DbMysql15",
                        db="DbMysql15",
                        port=3305)

    f = open("Tables//preview.json")
    urls = json.load(f)
    f.close()
    cur = DB.cursor()
    query = "ALTER TABLE test.SONGS \
           ADD COLUMN previewSong VARCHAR(300) NOT NULL DEFAULT '\"\"' AFTER trackPrice"

    cur.execute(query)
    DB.commit()

    for songId in urls:
        
        query = "UPDATE DbMysql15.Songs SET previewSong='%s' WHERE trackId='%s'"%(urls[songId], str(songId))
        cur.execute(query)
        
    DB.commit()

    #query = "ALTER TABLE test.artists \
     #       ADD COLUMN artistPicture VARCHAR(300) NOT NULL DEFAULT '\"\"' AFTER artistPrimaryGenre"

    #cur.execute(query)
    #DB.commit()
    f = open("Tables//pictures.json")
    pictures = json.load(f)
    f.close()

    for artist in pictures:
        artistToInsert = artist.replace("\\","")
        artistToInsert = artistToInsert.replace('"', "")
        try:
            query = "UPDATE DbMysql15.Artists SET artistPicture='%s' WHERE artistName='%s'"%(pictures[artist], artistToInsert)
            cur.execute(query)
        except:
            print(artistToInsert)
            continue
    DB.commit()
    

if __name__ == "__main__":
    main()
