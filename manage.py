'''
오로지 실행파일.
모든 설정은 세팅 폴더 안에서 관리 됨.
'''
from settings.settings import app, HOST_ADDR, SERVER_PORT, DEBUG, MODE
from waitress import serve
from paste.translogger import TransLogger


if __name__ == '__main__':
    if MODE == 'DEV':
        app.run(host=HOST_ADDR, port=SERVER_PORT, debug=DEBUG)
    elif MODE == 'RUN':
        serve(TransLogger(app, setup_console_handler=True),
              host=HOST_ADDR, port=SERVER_PORT)
