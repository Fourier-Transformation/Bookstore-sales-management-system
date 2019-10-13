"""
bookstore database instance
"""

from .utils import config as _config_parser
from . import connector as _connector


CONFIG_PATH = 'config.ini'


class BookStoreDataBase(object):
    """
    support an interface with database without SQL
    THIS CLASS SHOULD NOT HAVE MORE THAN ONE INSTANCE
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(BookStoreDataBase, cls).__new__(
                cls, *args, **kwargs)
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
        return sql_result

    def get_book_isbn(self, isbn: str) -> list:
        """
        return a list of book selected by ISBN
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE isbn = '%s'
            ''' % (isbn)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result

    def get_book_name(self, name: str) -> list:
        """
        return a list of book selected by name
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%s'
            ''' % (name)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result

    def get_book_name_part(self, name: str) -> list:
        """
        return a list of book selected by %name%
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%{0}%'
            '''.format(name)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result


# the only instance of BSDB
BOOKSTORE_DATABASE = BookStoreDataBase()
