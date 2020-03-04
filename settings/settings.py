import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# define
HOST_ADDR = '127.0.0.1'  # localhost 주소
SERVER_PORT = '8000'  # 서버 포트
DEBUG = False  # 디버그모드
MODE = os.environ.get('MODE')

# connect db
USER = 'postgres'  # username
PASSWOLRD = 'root'  # postgresql pw
DB_PORT = '5432'  # postgresql port
NAME = 'test'  # db name
POSTGRESQL = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{DB_PORT}/{NAME}'  # postgresql uri


# app settings
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

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


# manager
app.debug = DEBUG  # 실행 모드에 따라 디버그 온오프
db = SQLAlchemy(app)


# connect models
from .models import *


# connect urls
from .urls import *
