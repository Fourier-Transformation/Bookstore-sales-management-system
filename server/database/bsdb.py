"""
bookstore database instance
"""

from utils import config as _config_parser
from . import connector as _connector


CONFIG_PATH = 'config.ini'


class BSDB(object):
    """
    support an interface with database without SQL
    THIS CLASS SHOULD NOT HAVE MORE THAN ONE INSTANCE
    """

    def __init__(self):
        self._my_connect = _connector.BookStoreDatabaseConnector(
            *_config_parser.load(CONFIG_PATH, 'database_connection_info'))
        if self._my_connect == None:
            raise Exception('connect to database failed')

    def get_book_all(self) -> list:
        """
        return all the book list
        """
        pass

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
