import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from login import urls as loginurls
from account import urls as accounturls

# define
HOST_ADDR = '127.0.0.1'
PORT_NUM = '8000'
DEBUG = False

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

# select operation mode
def set_db():
    # todo make db setting func
    return 0


if os.environ.get('MODE') == 'DEV':  # mode - development
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif os.environ.get('MODE') == 'RUN':  # mode - release
    HOST_ADDR = '0.0.0.0'
    DEBUG = False
elif os.environ.get('MODE') == 'SET':  # mode - db set
    set_db()
else:  # select not permission mode
    raise Exception('MODE error')



if __name__ == '__main__':
    app.register_blueprint(loginurls.app, url_prefix='/login')
    app.register_blueprint(accounturls.app, url_prefix='/account')
    app.run(host=HOST_ADDR, port=PORT_NUM, debug=DEBUG)
