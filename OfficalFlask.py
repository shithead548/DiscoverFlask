from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<username>')
def show(username):
    return 'User %s' % username


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print url_for('hello_world')
    print url_for('about')

if __name__ == '__main__':
    app.run()
