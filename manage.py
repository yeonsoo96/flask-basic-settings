import time

from flask import request
from flask_sqlalchemy import SQLAlchemy
from gevent.pywsgi import WSGIServer

from settings.logger import logger
from settings.settings import HOST_ADDR, SERVER_PORT, MODE
from settings.wsgi import create_wsgi

app = create_wsgi()

# manager
db = SQLAlchemy(app)  # connect db
if __name__ == '__main__':
    if MODE == 'DEV':
        app.run(host=HOST_ADDR, port=SERVER_PORT)
    elif MODE == 'RUN':
        app = WSGIServer((HOST_ADDR, SERVER_PORT), app, log=None)
        app.serve_forever()


@app.after_request
def after_request(response):  # 리스폰스를 반환하면서 로그를 남김
    logger.info(f'{request.remote_addr} {time.strftime("%Y-%m-%d  %X", time.localtime(time.time()))}  '
                f'{request.method} {request.url} {response.status_code} - {request.user_agent}')
    return response
