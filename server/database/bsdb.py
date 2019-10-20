"""
bookstore database instance
"""

from decimal import Decimal as _Decimal
import time as _time
from .utils import config as _config_parser
from . import connector as _connector


CONFIG_PATH = 'config.ini'


class BookStoreDataBase(object):
    """
    support an interface with database without SQL
    THIS CLASS SHOULD NOT HAVE MORE THAN ONE INSTANCE
    """
    #column names of result, DOES NOT guarantee these tuples have right orders
    #all this constant is used for reference by this module only
    #every first element from the methods' result give you right orders
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
        10: 'publish_date'
        }
    RECORDS_NAMES_USER = {
        0: 'user_id',
        1: 'password',
        2: 'username',
        3: 'role',
        4: 'email'
        }
    RECORDS_NAMES_ORDER = {
        0: 'order_id',
        1: 'book_id',
        2: 'user_id',
        3: 'isbn',
        4: 'count',
        5: 'total_price',
        6: 'order_date',
        7: 'send_data'
        }

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
        return a pair of tuple and list
        tuple has talbe's column names
        list of tuples which represent all the books
        one tuple one record
        """
        sql_expr = \
            '''
            SELECT * FROM Books;
            '''
        sql_result = self._my_connect.execute_sql_read(sql_expr)
        return sql_result

    def get_book_isbn(self, isbn: str) -> (tuple, list):
        """
        return a list of book selected by ISBN
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE isbn = '%s'
            ''' % (isbn)
        sql_result = self._my_connect.execute_sql_read(sql_expr)
        return sql_result

    def get_book_name(self, name: str) -> (tuple, list):
        """
        return a list of book selected by name
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%s'
            ''' % (name)
        sql_result = self._my_connect.execute_sql_read(sql_expr)
        return sql_result

    def get_book_name_part(self, name: str) -> (tuple, list):
        """
        return a list of book selected by %name%
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE name = '%{0}%'
            '''.format(name)
        sql_result = self._my_connect.execute_sql_read(sql_expr)
        return sql_result

    def get_book_random(self) -> (tuple, list):
        """
        return a random book
        """
        sql_expr = \
            '''
            SELECT * FROM Books WHERE book_id >=
	        (SELECT FLOOR(MAX(book_id) * RAND()) FROM Books)
            LIMIT 1;
            '''
        sql_result = self._my_connect.execute_sql_read(sql_expr)
        return sql_result

    def insert_book(self, isbn: str, name: str, author: str, publisher: str,\
        price: _Decimal, amount: int, publish_date: _time.struct_time, **option_info):
        """
        insert a record to database
        @param option_info's key = { cover, category, description }
        """
        current_num = self._my_connect.execute_sql_read(
            '''
            SELECT MAX(book_id) FROM Books;
            '''
        )[1][0][0]
        if current_num is None:
            current_num = 0
        else:
            current_num = int(current_num)
        book_id = current_num + 1
        cover = None
        category = None
        description = None

        vals = [book_id, isbn, name, author, publisher, price, amount, publish_date]

        if 'cover' in option_info and isinstance(option_info['cover'], str):
            cover = option_info['cover']
            vals.append(cover)
        if 'category' in option_info and isinstance(option_info['category'], str):
            category = option_info['category']
            vals.append(category)
        if 'description' in option_info and isinstance(option_info['description'], str):
            description = option_info['description']
            vals.append(description)

        sql_expr = \
            '''
            INSERT INTO Books
                (book_id,isbn,name,author,publisher,price,amount,publish_date{0}{1}{2})
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s{3}{4}{5});
            '''.format(
                '' if cover is None else ',cover',
                '' if category is None else ',category',
                '' if description is None else ',description',

                '' if cover is None else ',%s',
                '' if category is None else ',%s',
                '' if description is None else ',%s'
            )

        # print(sql_expr) #debug
        self._my_connect.execute_sql_write(sql_expr,vals)



# the only instance of BSDB
BOOKSTORE_DATABASE = BookStoreDataBase()
