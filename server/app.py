from flask import Flask
app = Flask(__name__)


@app.route('/hello')  # which URL can trigger function
def hello_world():
    return 'hello,world!'


@app.route('/')  # root
def index():
    return 'Index Page'


@app.route('/user/<username>')  # variable rules: <variable name>
def show_user_profile(username: str):
    return 'User %s' % username


# choose the type of variable: <converter:variable name>
@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    return 'Post %d' % post_id


if __name__ == '__main__':  # ensure that it can't execute automaticly when importing
    app.run(debug=True)  # debug model
