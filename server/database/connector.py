"""
connector module
using this module in bookstoreDB only, do some SQL connection
"""
import mysql.connector as _mysql_connector


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

    def __del__(self):
        """
        destructor
        close database connection properly when shutdown the server
        """
        self.__bsdb.close()

    def __connect_to_db(self):
        """
        private method using host,username,passwd information to connect to mysql server
        """

        # bsdb = bookstore database mysql.connector.MySQLConnection instance
        # check if there is unclosed session
        if self.__bsdb is not None:
            if isinstance(self.__bsdb, _mysql_connector.MySQLConnection):
                self.__bsdb.close()

        # start new session
        try:
            self.__bsdb = _mysql_connector.connect(
                host=self.__host,
                user=self.__username,
                passwd=self.__passwd,
                database=self.__database
            )
        except:
            # something should write into log file
            print('Login mysql server ERROR')
            raise

    def execute_sql_read(self, sql: str, multi=False) -> (tuple, list):
        """
        execute sql to read and return result
        """
        mycursor = self.__bsdb.cursor()
        mycursor.execute(sql, None, multi=multi)

        names = mycursor.column_names
        records = []
        for x in mycursor:
            records.append(x)

        mycursor.close()

        return names, records

    def execute_sql_write(self, sql: str, val: tuple):
        """
        execute sql to write and not return
        @param sql SQL expression, using %s to replace the actual values
        @param val a tuple of actual values of sql
        """
        try:
            mycursor = self.__bsdb.cursor()
            mycursor.execute(sql, val)

            self.__bsdb.commit()

            mycursor.close()
        except Exception as e:
            print('[error] ' + str(e))

    def execute_sql_write_multiple(self, sql: str, vals: list):
        """
        execute sql to write multiple records
        @param sql SQL expression, using %s to replace the actual values
        @param val a list of tuple of actual values of sql
        """
        try:
            mycursor = self.__bsdb.cursor()
            mycursor.executemany(sql, vals)

            self.__bsdb.commit()

            mycursor.close()
        except Exception as e:
            print('[error] ' + str(e))
