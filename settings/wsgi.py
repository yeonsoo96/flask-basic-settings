import time

from flask import Flask, request
from flask_cors import CORS

from api.server import app as api_server
from api.test import app as api_test
from settings.logger import logger
from settings.settings import DEBUG, POSTGRESQL

# app settings
app = Flask(__name__)
app.debug = DEBUG  # debug mode
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# app connections
app.register_blueprint(api_server)
app.register_blueprint(api_test)


@app.after_request
def after_request(response):  # 리스폰스를 반환하면서 로그를 남김
    logger.info(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))}  '
                f'{request.method} {request.url} {response.status_code} - {request.user_agent}')
    return response
