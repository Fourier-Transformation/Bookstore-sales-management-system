from database.bsdb import BOOKSTORE_DATABASE as bd  # an object to interate with DB
from .preproc import books_to_dict  # include preprocessing of data


def get_book_list():
    """
    return json format of book list
    """
    header, records = bd.get_book_all()
    return books_to_dict(header, records)


def search_book_by_isbn(isbn: str):
    """
    return json format of a book by ISBN
    """
    header, records = bd.get_book_isbn(isbn)
    return books_to_dict(header, records)


def search_book_by_name(name: str):
    """
    return json format of a book by name
    """
    header, records = bd.get_book_name(name)
    return books_to_dict(header, records)


def search_book_by_keyword(keyword: str):
    """
    return json format of a book by keyword
    """
    header, records = bd.get_book_name_part(keyword)
    return books_to_dict(header, records)
