import logging
import os
import sys

from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from api.server import app as api_server
from api.test import app as api_test

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# define
HOST_ADDR = '127.0.0.1'  # localhost address
SERVER_PORT = 8000  # 서버 포트
DEBUG = False  # 디버그모드
MODE = os.environ.get('MODE')

# connect db
USER = 'postgres'  # username
PASSWOLRD = 'root'  # postgresql pw
DB_PORT = '5432'  # postgresql port
NAME = 'test'  # db name
POSTGRESQL = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{DB_PORT}/{NAME}'  # postgresql uri


# select operation mode
if MODE == 'TEST' or sys.argv[0].endswith('test'):  # use only pytest
    HOST_ADDR = '127.0.0.1'
    DEBUG = False
elif MODE == 'DEV':  # mode - development
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif MODE == 'RUN':  # mode - release
    HOST_ADDR = '0.0.0.0'
    DEBUG = False
else:  # select not permission mode
    raise KeyError


# app settings
app = Flask(__name__)
app.debug = DEBUG  # debug mode
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['LOGGING_LEVEL'] = logging.DEBUG
CORS(app)
logger = logging.getLogger('my_logger')

# @app.after_request
# def after_request(response):
#     # timestamp = strftime('[%Y-%b-%d %H:%M]')
#     logging.info(f'{request}')
#     return response
#
# @app.before_request
# def before_request():
#     pass


# app connections
app.register_blueprint(api_server)
app.register_blueprint(api_test)


# manager
db = SQLAlchemy(app)


