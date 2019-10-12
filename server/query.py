from database.bsdb import BOOKSTORE_DATABASE as bd


def get_book_list():
    """
    return json format of book list
    """
    return bd.get_book_all()


def search_book_by_isbn(isbn: str):
    """
    return json format of a book by ISBN
    """
    result = bd.get_book_isbn(isbn)
    print(result)
    return result


def search_book_by_name(name: str):
    """
    return json format of a book by name
    """
    result = bd.get_book_name(name)
    print(result)
    return result


def search_book_by_keyword(keyword: str):
    """
    return json format of a book by keyword
    """
    result = bd.get_book_name_part(keyword)
    print(result)
    return result
