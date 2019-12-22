import os
from flask import Flask, request
from werkzeug.utils import redirect


# define
HOST_ADDR = '127.0.0.1'
PORT_NUM = '8080'
DEBUG = False

app = Flask(__name__)
if os.environ.get('MODE') == 'DEV':
    HOST_ADDR = '0.0.0.0'
    DEBUG = True
else:
    raise Exception('MODE error')

@app.route("/", methods=['GET', 'POST'])
def hello():
    response = request.form['test']  # get body
    response += request.headers.get('test')  # get header
    # return redirect('user/yeonsookim')
    return response

@app.route('/user/<string:username>')
@app.route('/name/<string:username>')
def profile(username):
    return '{}\'s profile'.format(username)

if __name__ == '__main__':

    app.run(host=HOST_ADDR, port=PORT_NUM, debug=DEBUG)