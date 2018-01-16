import MySQLdb as sql
import logging
import os
import json

def main():
    DB = sql.connect(host="localhost",
                        user="root",
                        passwd="6464",
                        db="test",
                        port=3306)

    f = open("preview.json")
    urls = json.load(f)
    f.close()
    cur = DB.cursor()
    query = "ALTER TABLE test.SONGS \
            ADD COLUMN previewSong VARCHAR(300) NOT NULL DEFAULT '\"\"' AFTER trackPrice"

    cur.execute(query)
    DB.commit()

    for songId in urls:
        
        query = "UPDATE test.songs SET previewSong='%s' WHERE trackId='%s'"%(urls[songId], str(songId))
        cur.execute(query)
        
    DB.commit()

    query = "ALTER TABLE test.artists \
            ADD COLUMN artistPicture VARCHAR(300) NOT NULL DEFAULT '\"\"' AFTER artistPrimaryGenre"

    cur.execute(query)
    DB.commit()
    f = open("pictures.json")
    pictures = json.load(f)
    f.close()

    for artist in pictures:
        artistToInsert = artist.replace("\\","")
        artistToInsert = artistToInsert.replace('"', "")
        try:
            query = "UPDATE test.artists SET artistPicture='%s' WHERE artistName='%s'"%(pictures[artist], artistToInsert)
            cur.execute(query)
        except:
            print(artistToInsert)
            continue
    DB.commit()
    

if __name__ == "__main__":
    main()