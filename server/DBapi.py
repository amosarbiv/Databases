import MySQLdb as sql
import logging
import os

class DB():
    def __init__(self):

        logging.basicConfig(fillename="API.log", level=logging.DEBUG)
        self.logger = logging.getLogger("DBapi")
        
        try:
            self.DB = sql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    db="DbMysql15",
                                    port=3305)
        except Exception as e:
            self.logger.error("Error in logging to DB: %s"%str(e))
            os._exit(0)
        
        self.cur = self.DB.cursor() 

    def checkPass(self,gotUser, gotPasswd):
        results = self.cur.excute("SELECT Users.user, Users.password FROM Users \
                        WHERE %s=Users.user"%gotUser)

        if ( len(results) == 0 ):
            return -1 #meaning no such user 
        
        if ( len(results) > 1 ):
            self.logger.error("got more than one user...its a problem")
            return None

        (user, passwd) = results[0]
        if ( gotPasswd == passwd ):
            return True
        else:
            return False