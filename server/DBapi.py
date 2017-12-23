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

    def CreateUser(self, user, password, firstName, lastName, age, country, radioButton):
        userExist = self.CheckUserLogin(user, password)
        if(userExist != -1):
            print("There is user")
            return False
        else:
            query = "INSERT INTO test.userlogin (userName, userPass, firstName, lastName, age, country, gender) VALUES ('{}', '{}', '{}', '{}', {}, '{}', '{}');".format(user, password, firstName, lastName, age, country, radioButton)
            try:
                self.cur.execute(query)
                self.DB.commit()
                return True
            except:
                self.DB.rollback()
                return False

    def CheckUserLogin(self, userName, password):
        query = "SELECT userLogin.userName, userLogin.userPass FROM userLogin WHERE userLogin.userName='%s'"%userName
        self.cur.execute(query)
        results = self.cur.fetchall()
        if ( len(results) == 0 ):
            return -1 #meaning no such user 

        (user, passwd) = results[0]
        if ( password == passwd ):
            return True
        else:
            return False
