import MySQLdb
import json
import os

cursor = MySQLdb.connect('localhost', db='DbMysql15', user='DbMysql15', password='DbMysql15', port=3305)
NUMBER_OF_TABLES = 7
absPath = os.path.dirname(__file__) #<-- absolute dir the script is in
  
try:
    rel_path = 'Tables/ArtistsTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    ArtistsTable = json.load(json_data)

    rel_path = 'Tables/UsersTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    UsersTable = json.load(json_data)

    rel_path = 'Tables/SongsTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    SongsTable = json.load(json_data)

    rel_path = 'Tables/CollectionTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    CollectionsTable = json.load(json_data)

    rel_path = 'Tables/TrackUserTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    TrackUserTable = json.load(json_data)

    rel_path = 'Tables/ArtistUserTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    ArtistRankingTable = json.load(json_data)

    rel_path = 'Tables/ArtistCollectionTable.json'
    fullPath = os.path.join(absPath, rel_path)
    json_data = open(fullPath, 'r')
    ArtistCollectionTable = json.load(json_data)
    
    cursor2=cursor.cursor()
    
    rel_path = 'CREATE-DB-SCRIPT.sql'
    fullPath = os.path.join(absPath, rel_path)
    createDbSqlScript = open(fullPath, 'r')

    # Use the SQL script to create the tables
    for i in range(NUMBER_OF_TABLES):
            createJson = createDbSqlScript.readline()
            print(createJson)
            cursor.query(createJson)
    createDbSqlScript.close()


	# Add columns to each table and fill it with data
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
    

