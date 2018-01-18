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
    json_data = open('Tables//ArtistUserTable.json')
    ArtistRankingTable = json.load(json_data)
    json_data = open('Tables//ArtistCollectionTable.json')
    ArtistCollectionTable = json.load(json_data)
    

    cursor2=cursor.cursor()
    
    
    """print("connected")
    DropTable = "DROP TABLE TrackUser;"
    cursor.query(DropTable)
    cursor.commit()
    print("Drop success")
    DropTable = "DROP TABLE CollectionsArtist;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE ArtistUser;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Users;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Songs;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Collections;"
    cursor.query(DropTable)
    DropTable = "DROP TABLE Artists;"
    cursor.query(DropTable)"""

    createJson = "CREATE TABLE Artists (artistId int NOT NULL, artistName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, artistPrimaryGenre varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, PRIMARY KEY(artistId));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE Users (userName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, userPassword varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, userFirstName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI, userLastName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, userCountry varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, userGender varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, userAge int NOT NULL, playlistPrivacy INT NOT NULL, PRIMARY KEY(userName));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE Collections (collectionId int NOT NULL, collectionName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, collectionReleaseDate Date NOT NULL, collectionPrice int NOT NULL, country varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, collectionGenre varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, numberOfTracks int NOT NULL, PRIMARY KEY(collectionId));"
    cursor.query(createJson)
    
    createJson = "CREATE TABLE CollectionsArtist (indexm int NOT NULL AUTO_INCREMENT, collectionId int NOT NULL, artistId int NOT NULL, FOREIGN KEY(collectionId) REFERENCES Collections(collectionId), FOREIGN KEY(artistId) REFERENCES Artists(artistId), PRIMARY KEY(indexm));"
    cursor.query(createJson)
    
    createJson = "CREATE TABLE Songs (trackId int NOT NULL, trackName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, collectionId int NOT NULL, discNumber int NOT NULL, trackPosition int NOT NULL, trackReleaseDate Date NOT NULL, trackTimeMillis int NOT NULL, trackGenre varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, trackPrice int NOT NULL, FOREIGN KEY(collectionId) REFERENCES Collections(collectionId), PRIMARY KEY (trackId));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE TrackUser(trackId int NOT NULL, userName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, numberOfViews int NOT NULL, ranking int NOT NULL, isInPlaylist INT NOT NULL, FOREIGN KEY (trackId) REFERENCES Songs(trackId), FOREIGN KEY (userName) REFERENCES Users(userName), PRIMARY KEY(trackId, userName));"
    cursor.query(createJson)
	
    createJson = "CREATE TABLE ArtistUser (artistId int NOT NULL, userName varchar(250) CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI NOT NULL, artistRanking int NOT NULL, FOREIGN KEY (artistId) REFERENCES Artists(artistId), FOREIGN KEY (userName) REFERENCES Users(userName));"
    cursor.query(createJson)
    cursor.commit()
    print("create success")
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


    columns_names = ["userName", "userPassword", "userFirstName", "userLastName", "userCountry", "userGender", "userAge", "playlistPrivacy"]
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
    
    columns_names = ["trackId", "userName", "numberOfViews", "ranking", "isInPlaylist"]
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
        sql = ("INSERT INTO ArtistUser ({columns_names}) "
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
    

