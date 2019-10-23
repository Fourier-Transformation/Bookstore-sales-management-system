from flask import Flask, redirect, request, url_for
import json
from proc import query

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../build',
)


@app.route('/')  # root
def index():
    """
    return index page
    """
    return app.send_static_file('index.html')


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


@app.route('/api/books/')
def get_books():
    return redirect(url_for('show_books'))


@app.route('/books/')
def show_books():
    """
    show a list of all the books
    """
    result = {'books': query.get_book_list()}
    return json.dumps(result, ensure_ascii=False)


@app.route('/api/books/isbn/<string:isbn>')
def get_books_by_isbn(isbn):
    return redirect(url_for('show_books_by_isbn', isbn=isbn))


@app.route('/books/isbn/?<string:isbn>')
def show_books_by_isbn(isbn):
    result = {'books': query.search_book_by_isbn(isbn)}
    return json.dumps(result, ensure_ascii=False)


@app.route('/api/books/page/<int:page>')
def get_books_by_page(page=1):
    return redirect(url_for('show_books_by_page', page=page))


@app.route('/books/page/?<int:page>')
def show_books_by_page(page):
    """
    show a part of books devided by page
    """
    result = {'books': query.get_book_list()}
    return json.dumps(result, ensure_ascii=False)


@app.route('/api/books/name/<string:name>')
def get_books_by_name(name):
    return redirect(url_for('show_books_by_name', name=name))


@app.route('/books/name/?<string:name>')
def show_books_by_name(name):
    result = query.search_book_by_keyword(name)
    return json.dumps(result, ensure_ascii=False)


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


if __name__ == '__main__':
    #app.config['JSON_AS_ASCII'] = False
    #app.config['json.dumps_PRETTYPRINT_REGULAR'] = True
    app.run(debug=False, port=37373)  # ~~37373外部端口~~
