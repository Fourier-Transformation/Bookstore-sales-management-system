"""
bookstore database instance
"""

import utils.config as _config_parser
from . import connector as _connector


CONFIG_PATH = 'config.ini'

class BSDB(object):
    """
    support an interface with database without SQL
    THIS CLASS SHOULD NOT HAVE MORE THAN ONE INSTANCE
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(BSDB, cls).__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self):
        self._my_connect = _connector.BookStoreDatabaseConnector(
            *_config_parser.load(CONFIG_PATH, 'DATABASE_CONNECTION'))
        if self._my_connect is None:
            raise Exception('connect to database failed')

    def get_book_all(self) -> list:
        """
        return a list of tuples which represent all the books
        one tuple one record
        """
        sql_expr = \
            '''
            SELECT * FROM Books;
            '''
        sql_result = self._my_connect.execute_sql(sql_expr)
        print(sql_result)

    def get_book_isbn(self, isbn: str) -> list:
        """
        return a list of book selected by ISBN
        """
        pass

    def get_book_name(self, name: str) -> list:
        """
        return a list of book selected by name
        """
        pass

if __name__ == '__main__':
    db = BSDB()
    print(db.get_book_all())
