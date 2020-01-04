from flask.views import MethodView
from flask import request
from .models import User

class AccountUser(MethodView):
    def get(self):
        response = dict(request.headers)
        return response

    def post(self):
        return 'post'