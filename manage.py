from paste.translogger import TransLogger
from waitress import serve

from settings.settings import app, HOST_ADDR, SERVER_PORT, MODE

if __name__ == '__main__':
    if MODE == 'DEV':
        app.run(host=HOST_ADDR, port=SERVER_PORT)
    elif MODE == 'RUN':
        serve(TransLogger(app, setup_console_handler=True),
              host=HOST_ADDR, port=SERVER_PORT)
