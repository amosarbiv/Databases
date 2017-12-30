import MySQLdb
import json

cursor = MySQLdb.connect('localhost', db='test', user='root', password='LA1026vi', port=3306)
  
try:
    json_data = open('Tables//ArtistsTable.json')
    ArtistsTable = json.load(json_data)
    json_data = open('Tables//UsersTable.json')
    UsersTable = json.load(json_data)
    json_data = open('Tables//SongsTable.json')
    SongsTable = json.load(json_data)
    json_data = open('Tables//CollectionTable.json')
    CollectionsTable = json.load(json_data)
    json_data = open('Tables//TrackUserTable.json')
    TrackUserTable = json.load(json_data)
    json_data = open('Tables//ArtistRankingTable.json')
    ArtistRankingTable = json.load(json_data)
    json_data = open('Tables//ArtistCollectionTable.json')
    ArtistCollectionTable = json.load(json_data)
    
    
    cursor2=cursor.cursor()
    
    DropTable = "DROP TABLE TrackUser;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE CollectionsArtist;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE ArtistRanking;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Users;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Songs;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Collections;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Artists;"
    cursor.query(DropTable)
    
	
    createJson = "CREATE TABLE Artists (artistId int NOT NULL, artistName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, artistPrimaryGenre varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, PRIMARY KEY(artistId));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE Users (userName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, password varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, firstName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, lastName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, country varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, gender varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, age int NOT NULL, privacy BIT NOT NULL, PRIMARY KEY(userName));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE Collections (collectionId int NOT NULL, collectionName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, collectionReleaseDate Date NOT NULL, collectionPrice int NOT NULL, country varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, collectionGenre varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, numberOfTracks int NOT NULL, PRIMARY KEY(collectionId));"
    cursor.query(createJson)
    
    createJson = "CREATE TABLE CollectionsArtist (indexm int NOT NULL AUTO_INCREMENT, collectionId int NOT NULL, artistId int NOT NULL, FOREIGN KEY(collectionId) REFERENCES Collections(collectionId), FOREIGN KEY(artistId) REFERENCES Artists(artistId), PRIMARY KEY(indexm));"
    cursor.query(createJson)
    
    createJson = "CREATE TABLE Songs (trackId int NOT NULL, trackName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, collectionId int NOT NULL, discNumber int NOT NULL, trackPosition int NOT NULL, trackReleaseDate Date NOT NULL, trackTimeMillis int NOT NULL, trackGenre varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, trackPrice int NOT NULL, FOREIGN KEY(collectionId) REFERENCES Collections(collectionId), PRIMARY KEY (trackId));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE TrackUser(trackId int NOT NULL, userName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, numberOfViews int NOT NULL, trackRank int NOT NULL, isInPlaylist BIT NOT NULL, FOREIGN KEY (trackId) REFERENCES Songs(trackId), FOREIGN KEY (userName) REFERENCES Users(userName), PRIMARY KEY(trackId, userName));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE ArtistRanking (artistId int NOT NULL, userName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL, artistRanking int NOT NULL, FOREIGN KEY (artistId) REFERENCES Artists(artistId), FOREIGN KEY (userName) REFERENCES Users(userName));"
    cursor.query(createJson)
	
    columns_names = ["artistId", "artistName", "artistPrimaryGenre"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in ArtistsTable:
        sql = ("INSERT INTO Artists ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
    
	
    columns_names = ["collectionId", "collectionName", "collectionReleaseDate", "collectionPrice", "country", "collectionGenre", "numberOfTracks"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in CollectionsTable:
        data_dict["collectionReleaseDate"]=data_dict["collectionReleaseDate"][:10]
        sql = ("INSERT INTO Collections ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["trackId", "trackName", "collectionId", "discNumber", "trackPosition", "trackReleaseDate", "trackTimeMillis",  "trackGenre", "trackPrice"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in SongsTable:
        data_dict["trackReleaseDate"]=data_dict["trackReleaseDate"][:10]
        sql = ("INSERT INTO Songs ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")


    columns_names = ["userName", "password", "firstName", "lastName", "country", "gender", "age", "privacy"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in UsersTable:
        sql = ("INSERT INTO Users ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
    
    columns_names = ["trackId", "userName", "numberOfViews", "trackRank", "isInPlaylist"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in TrackUserTable:
        sql = ("INSERT INTO TrackUser ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["artistId", "userName", "artistRanking"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in ArtistRankingTable:
        sql = ("INSERT INTO ArtistRanking ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")

    columns_names = ["artistId", "collectionId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in ArtistCollectionTable:
        sql = ("INSERT INTO CollectionsArtist ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
    cursor.commit()
finally:
    cursor.close()
    

