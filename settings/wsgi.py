import time
import traceback

from flask import Flask
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from api.server import app as api_server
from api.test import app as api_test
from settings.logger import create_logger
from settings.settings import DEBUG, POSTGRESQL

logger = create_logger()


def after_request(response):  # 정상적으로 처리시 로그를 남김
    logger.info(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))}  '
                f'{request.method} {request.url} {response.status_code} - {request.user_agent}')
    return response


def trace_back_recent_call():  # 오류가 난 코드의 위치를 스트링으로 반환함.
    error_location = traceback.format_exc().split('\n')[15]
    return error_location


def error_handler(error):  # 에러 발생시 로그를 남김
    logger.error(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))} '
                 f'{request.method} {request.url} {error.code} - {request.user_agent} \n {trace_back_recent_call()}')


def create_wsgi():
    # app settings
    app = Flask(__name__)
    app.debug = DEBUG  # debug mode
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.after_request(after_request)
    app.register_error_handler(HTTPException, error_handler)
    CORS(app)

    # app connections
    app.register_blueprint(api_server)
    app.register_blueprint(api_test)
    return app
