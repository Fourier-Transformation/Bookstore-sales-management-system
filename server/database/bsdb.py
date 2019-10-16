"""
bookstore database instance
"""

from decimal import Decimal
from time import time
from .utils import config as _config_parser
from . import connector as _connector


CONFIG_PATH = 'config.ini'


class BookStoreDataBase(object):
    """
    support an interface with database without SQL
    THIS CLASS SHOULD NOT HAVE MORE THAN ONE INSTANCE
    """

    """
    column names of result, does not guarantee these tuples have right orders
    all this constant is used for reference by this module only
    every first element from the methods' result give you right orders
    """
    RECORDS_NAMES_BOOK = { 
        0: 'book_id', 
        1: 'isbn', 
        2: 'name', 
        3: 'author', 
        4: 'publisher', 
        5: 'price',
        6: 'cover', 
        7: 'category', 
        8: 'amount', 
        9: 'description', 
        10: 'publish_date' }
    RECORDS_NAMES_USER = ('user_id', 'password', 'username', 'role', 'email')
    RECORDS_NAMES_ORDER = ('order_id', 'book_id', 'user_id', 'isbn', 'count',\
         'total_price', 'order_date', 'send_data')

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

    def get_book_all(self) -> (tuple, list):
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

    def get_book_isbn(self, isbn: str) -> (tuple, list):
        """
        return a list of book selected by ISBN
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE isbn = '%s'
            ''' % (isbn)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result

    def get_book_name(self, name: str) -> (tuple, list):
        """
        return a list of book selected by name
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%s'
            ''' % (name)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result

    def get_book_name_part(self, name: str) -> (tuple, list):
        """
        return a list of book selected by %name%
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%{0}%'
            '''.format(name)
        sql_result = self._my_connect.execute_sql(sql_expr)
        return sql_result

    def insert_book(self, book_id: int, isbn: str, name: str, author: str, publisher: str,\
        price: Decimal, amount: int, publish_date: time, **option_info) -> (tuple, list):
        """
        insert a record to database
        @param option_info's key = { RECORDS_NAMES_BOOK[6 or 7 or 9] }
        """
        pass


# the only instance of BSDB
BOOKSTORE_DATABASE = BookStoreDataBase()
