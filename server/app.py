from flask import Flask, request
import config
import query

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')  # root
def index():
    """
    return index page
    """
    return 'Welcome to our online bookstore!'


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
    return 'User %s' % username


@app.route('/books/')
def show_books():
    """
    show a list of all the books
    """
    return query.get_book_list()


@app.route('/orders/')
def show_orders():
    """
    show a list of all the orders

    only Administrator permission
    """
    return 'hehe'


if __name__ == '__main__':  # ensure that it can't execute automaticly when importing
    app.run()
