import os
from flask import Flask, request, render_template
from werkzeug.utils import redirect
import login
from flask_sqlalchemy import SQLAlchemy


# define
HOST_ADDR = '127.0.0.1'
PORT_NUM = '8000'
DEBUG = False

app = Flask(__name__)
db = SQLAlchemy(app)

# select operation mode
if os.environ.get('MODE') == 'DEV':  # mode - development
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif os.environ.get('MODE') == 'RUN':  # mode - release
    HOST_ADDR = '0.0.0.0'
    DEBUG = False
else:  # select not permission mode
    raise Exception('MODE error')


@app.route("/", methods=['GET', 'POST'])
def call_login():
    return login.login()


def hello():
    # response = request.form['test']  # get body
    # response += request.headers.get('test')  # get header
    return redirect('login')
    # return response
    # return render_template('wink.html')


@app.route('/user/<string:username>')
@app.route('/name/<string:username>')
def profile(username):
    db.create_all()
    user = User(username+'@gmail.com')
    db.session.add(user)
    db.session.commit()
    return '{}\'s profile'.format(username)


@app.route('/user/')
def user():
    user = User.query.all()
    return str(user)


class User(db.Model):
    __table_name__ = 'user'
    email = db.Column(db.String(50), primary_key=True, unique=True)

    def __init__(self, email):
        self.email = email

    def info(self):
        return self.email


if __name__ == '__main__':
    app.run(host=HOST_ADDR, port=PORT_NUM, debug=DEBUG)
