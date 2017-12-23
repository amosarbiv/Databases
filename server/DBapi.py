import MySQLdb as sql
import logging
import os

class DB():
    def __init__(self, DBUserName, DBPasswd, DBName, DBPort=3306, DBhost="127.0.0.1"):

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("DBapi")
        
        try:
            self.DB = sql.connect(host=DBhost,
                                    user=DBUserName,
                                    passwd=DBPasswd,
                                    db=DBName,
                                    port=DBPort)
        except Exception as e:
            self.logger.error("Error in logging to DB: %s"%str(e))
            os._exit(0)
        
        self.cur = self.DB.cursor() 

    def CheckUserLogin(self, userName, password):
        query = "SELECT userLogin.UserName, userLogin.Password FROM userLogin WHERE userLogin.UserName='%s'"%userName
        self.cur.execute(query)
        results = self.cur.fetchall()
        if ( len(results) == 0 ):
            return -1 #meaning no such user 

        (user, passwd) = results[0]
        if ( password == passwd ):
            return True
        else:
            return False

    def CreateUser(self, user, password, firstName, lastName, age, country):
        userExist = CheckUserLogin(self, user, password)
        if(userExist != -1):
            return False
        else:
            query = "INSERT INTO test.userlogin (userName, userPass, firstName, lastName, age, country) VALUES ('%s', '%s', '%s', %s, '%s');"
            self.cur.execute(query, (user, password, firstName, lastName, age, country))