import MySQLdb
import json

cursor = MySQLdb.connect('localhost', db='sqldatabase15', user='root', password='THKfruc97##', port=3306)
  
try:
    json_data = open('Tables//ArtistsTable.json')
    ArtistsTable = json.load(json_data)
    json_data = open('Tables//AlbumArtistTable.json')
    AlbumArtistTable = json.load(json_data)
    json_data = open('Tables//AlbumSongsTable.json')
    AlbumSongsTable = json.load(json_data)
    json_data = open('Tables//AlbumTable.json')
    AlbumTable = json.load(json_data)
    json_data = open('Tables//ArtistSongTable.json')
    ArtistSongTable = json.load(json_data)
    json_data = open('Tables//Playlists.json')
    PlaylistsTable = json.load(json_data)
    json_data = open('Tables//Rankings.json')
    RankingsTable = json.load(json_data)
    json_data = open('Tables//SongsTable.json')
    SongsTable = json.load(json_data)
    json_data = open('Tables//UserPlaylists.json')
    UserPlaylistsTable = json.load(json_data)
    json_data = open('Tables//UsersTable.json')
    UsersTable = json.load(json_data)
    json_data = open('Tables//Views.json')
    ViewsTable = json.load(json_data)
    #print(jsonobject)
    cursor2=cursor.cursor()
    
    createJson = "CREATE TABLE Artists (artistId int, artistName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin);"
    cursor.query(createJson)
    createJson = "CREATE TABLE AlbumArtist (artistId int, collectionId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE AlbumSongs (trackId int, collectionId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE Album (collectionName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, collectionId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE ArtistSong (trackId int, artistId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE Playlists (playlistId int, userId int, privacy varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, trackId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE Rankings (ranking int, userId int, trackId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE Songs (primaryGenreName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, trackName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, trackTimeMillis int, releaseDate Date, trackId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE UserPlaylists (playlistId int, userId int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE Users (firstName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, lastName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, userId int, country varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, gender varchar(250) CHARACTER SET utf8 COLLATE utf8_bin, age int);"
    cursor.query(createJson)
    createJson = "CREATE TABLE UserViews (userId int, numOfViews int, trackId int);"
    cursor.query(createJson)

    columns_names = ["artistId", "artistName"]
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
	
    columns_names = ["artistId", "collectionId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in AlbumArtistTable:
        sql = ("INSERT INTO AlbumArtist ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["trackId", "collectionId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in AlbumSongsTable:
        sql = ("INSERT INTO AlbumSongs ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["collectionName", "collectionId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in AlbumTable:
        sql = ("INSERT INTO Album ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["trackId", "artistId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in ArtistSongTable:
        sql = ("INSERT INTO ArtistSong ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["playlistId", "userId", "privacy", "trackId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in PlaylistsTable:
        sql = ("INSERT INTO Playlists ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["ranking", "userId", "trackId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in RankingsTable:
        sql = ("INSERT INTO Rankings ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["primaryGenreName", "trackName", "trackTimeMillis", "releaseDate", "trackId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in SongsTable:
        data_dict["releaseDate"]=data_dict["releaseDate"][:10]
        sql = ("INSERT INTO Songs ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
	
    columns_names = ["firstName", "lastName", "userId", "country", "gender", "age"]
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
	
    columns_names = ["userId", "numOfViews", "trackId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in ViewsTable:
        sql = ("INSERT INTO UserViews ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")

    columns_names = ["playlistId", "userId"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in UserPlaylistsTable:
        sql = ("INSERT INTO UserPlaylists ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict[column] for column in columns_names]
        cursor2.execute(sql, values)
    print("Insert successfull!")
    cursor.commit()
finally:
    cursor.close()
    

