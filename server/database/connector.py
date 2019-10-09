"""
connector module
using this module in bookstoreDB only, do some SQL connection
"""
import mysql.connector


class BookStoreDatabaseConnector(object):
    """
    using to connect to mysql server, execute sql, return the result
    restart session if necessary
    """

    def __init__(self, host, username, passwd, database):
        """
        init object
        """
        self.__host = host
        self.__username = username
        self.__passwd = passwd
        self.__database = database

        self.__bsdb = None
        self.__connect_to_db()

    def __connect_to_db(self):
        """
        private method using host,username,passwd information to connect to mysql server
        """

        # bsdb = bookstore database mysql.connector.MySQLConnection instance
        # check if there is unclosed session
        if self.__bsdb is not None:
            if isinstance(self.bsdb, mysql.connector.MySQLConnection):
                self.__bsdb.close()

        # start new session
        try:
            self.__bsdb = mysql.connector.connect(
                host=self.__host,
                user=self.__username,
                passwd=self.__passwd,
                databse=self.__database
            )
        except:
            # something should write into log file
            print('Login mysql server ERROR')
            raise

    def execute_sql(self, sql: str) -> list:
        """
        execute sql and return result
        """
        mycursor = self.__bsdb.cursor()
        mycursor.execute(sql)

        result = []
        for x in mycursor:
            result.append(x)

        mycursor.close()

        return result
