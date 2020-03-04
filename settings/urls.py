'''
모든 앱의 접근 주소를 여기서 관리함.
여기에서 반드시 임포트와 레지스터 해줘야함.
앱에서만 유알엘을 추가한다고 적용되지 않음.
'''

from settings.settings import app
from login import urls as loginurls
from account import urls as accounturls
from flask import json, request, Response
import os


@app.route('/ping', methods=['GET'])
def ping():  # 서버 연결 테스트용
    return 'ping'


@app.route('/deploy', methods=['POST'])
def hooks():
    res = json.dumps(request.form)
    res = json.loads(res)
    res = json.loads(res['payload'])
    root_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    if res['ref'] == 'refs/heads/deploy':
        os.system(f'sh {root_dir}/settings/hooks.sh')
    return Response('push', status=200)


app.register_blueprint(loginurls.app, url_prefix='/login')  # /login으로 시작하면 login_app으로 연결
app.register_blueprint(accounturls.app, url_prefix='/account')