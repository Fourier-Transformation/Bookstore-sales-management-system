from flask import Flask, redirect, request, url_for, json, jsonify
from proc import query

app = Flask(__name__)


@app.route('/')  # root
def index():
    """
    return index page
    """
    return '欢迎光临！'


@app.route('/login/', methods=['get', 'post'])
def login():
    """
    return login page
    """
    return 'login page'


@app.route('/user/<username>')  # variable rules: <variable name>
def show_user_profile(username: str):
    """
    return user's profile
    param username: the ID of users
    """
    url = url_for('user', name=username)
    print(url)
    return redirect(url)


@app.route('/books/', defaults={'page': 1})
def show_books(page):
    """
    show a list of all the books
    """
    result = {'books': query.get_book_list()}
    return jsonify(result)


@app.route('/books/?<isbn>')
def show_books_by_isbn(isbn):
    result = {'books': query.search_book_by_isbn(isbn)}
    return jsonify(result)


@app.route('/books/query/<isbn>')
def get_books_by_isbn(isbn):
    return redirect(url_for('show_books_by_isbn', isbn=isbn))


@app.route('/books/<int:page>')
def show_books_by_page(page=1):
    """
    show a part of books devided by page
    """
    return redirect(url_for('show_books', page=page))


@app.route('/orders/')
def show_orders():
    """
    show a list of all the orders

    only Administrator permission
    """
    return 'hehe'


@app.route('/users/')
def show_users():
    """
    show a list of all the users

    only Administrator permission
    """
    return 'hehe'


if __name__ == '__main__':  # ensure that it can't execute automaticly when importing
    app.run(debug=True, port=37373)  # 37373外部端口


@app.route('/api/')
def get_api():
    pass
