import mysql.connector
from mysql.connector import errorcode
import json

try:
    cnx = mysql.connector.connect(user='root', password='LA1026vi',
                                  host='127.0.0.1',
                                  database='test')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  
try:
    json_data = open('Tables//ArtistsTable.json')
    jsonobject = json.load(json_data)
    #print(jsonobject)
    cursor = cnx.cursor()
    #createJson = "CREATE TABLE json_test (artistId varchar(250),artistName varchar(250) CHARACTER SET utf8 COLLATE utf8_bin);"
    #cursor.execute(createJson)

    columns_names = ["artistId", "artistName"]
    columns_names_str = ', '.join(columns_names)
    binds_str = ', '.join('%s' for _ in range(len(columns_names)))
    for data_dict in jsonobject:
        print(data_dict)
        sql = ("INSERT INTO json_test ({columns_names}) "
                "VALUES ({binds})"
                .format(columns_names=columns_names_str,
                        binds=binds_str))
        values = [data_dict["artistId"],data_dict["artistName"]]
        cursor.execute(sql, values)
    print("Insert successfull!")
    cnx.commit()
finally:
    cnx.close()
    

