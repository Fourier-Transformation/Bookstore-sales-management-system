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
    # column names of result, DOES NOT guarantee these tuples have right orders
    # all this constant is used for reference by this module only
    # every first element from the methods' result give you right orders
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

    def insert_book(self, isbn: str, name: str, author: str, publisher: str,
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

        val = [book_id, isbn, name, author,
               publisher, price, amount, publish_date]

        if 'cover' in option_info and isinstance(option_info['cover'], str):
            cover = option_info['cover']
            val.append(cover)
        if 'category' in option_info and isinstance(option_info['category'], str):
            category = option_info['category']
            val.append(category)
        if 'description' in option_info and isinstance(option_info['description'], str):
            description = option_info['description']
            val.append(description)

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
        self._my_connect.execute_sql_write(sql_expr, val)

    def insert_books(self, isbn: list, name: list, author: list, publisher: list,
                     price: list, amount: list, publish_date: list, **option_info):
        """
        insert multiple books records into data. data should be format as values in list
        input type:
            isbn: str in list/tuple
            name: str in list/tuple
            author: str in list/tuple
            publisher: str in list/tuple
            price: Decimal in list/tuple
            amount: int in list/tuple
            publish_date: time.struct_time in list/tuple
            option_info:
                'cover': str in list/tuple
                'category': str in list/tuple
                'description': str in list/tuple
        @param option_info's key = { cover, category, description }
        """
        # check if the length of every parameter is matched
        size = len(isbn)
        if size != len(name) or \
                size != len(author) or \
                size != len(publisher) or \
                size != len(price) or \
                size != len(amount) or \
                size != len(publish_date):
            raise Exception("length of parameters does not match")

        # arrange book_id
        current_num = self._my_connect.execute_sql_read(
            '''
            SELECT MAX(book_id) FROM Books;
            '''
        )[1][0][0]
        if current_num is None:
            current_num = 0
        else:
            current_num = int(current_num)
        book_id = [x for x in range(current_num + 1, current_num + size + 1)]

        # make up vals
        has_cover = False
        has_category = False
        has_description = False

        cover = None
        category = None
        description = None

        if 'cover' in option_info:
            has_cover = True
            cover = option_info['cover']
        if 'category' in option_info:
            has_category = True
            category = option_info['category']
        if 'description' in option_info:
            has_description = True
            description = option_info['description']

        vals = []
        for i in range(size):
            val = [book_id[i], isbn[i], name[i], author[i], publisher[i],
                   price[i], amount[i], publish_date[i]]
            if has_cover:
                val.append(cover[i])
            if has_category:
                val.append(category[i])
            if has_description:
                val.append(description[i])
            vals.append(val)

        sql_expr = \
            '''
            INSERT INTO Books
                (book_id,isbn,name,author,publisher,price,amount,publish_date{0}{1}{2})
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s{3}{4}{5});
            '''.format(
                '' if not has_cover else ',cover',
                '' if not has_category else ',category',
                '' if not has_description else ',description',

                '' if not has_cover else ',%s',
                '' if not has_category else ',%s',
                '' if not has_description else ',%s'
            )

        self._my_connect.execute_sql_write_multiple(sql_expr, vals)


# the only instance of BSDB
BOOKSTORE_DATABASE = BookStoreDataBase()
