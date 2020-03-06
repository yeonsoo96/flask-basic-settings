import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s : %(message)s')  # 로그 앞에 로그 레벨을 표시

file_handler = logging.FileHandler('LOG.log')  # 파일로 로그 저장
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()  # 콘솔에 로그 표시
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

flask_log = logging.getLogger('werkzeug')  # 기본 앱서버 로그 끔
flask_log.disabled = True

gevent_log = logging.getLogger('gevent')  # gevent 로그 끔
gevent_log.disabled = True