from gevent.pywsgi import WSGIServer

from settings.settings import app, HOST_ADDR, SERVER_PORT, MODE

if __name__ == '__main__':
    if MODE == 'DEV':
        app.run(host=HOST_ADDR, port=SERVER_PORT)
    elif MODE == 'RUN':
        app = WSGIServer((HOST_ADDR, SERVER_PORT), app)
        app.serve_forever()
