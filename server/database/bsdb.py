"""
bookstore database instance
"""


class BSDB(object):
    """
    support an interface with database without SQL
    """

    def __init__(self, config_path: str):
        pass

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
