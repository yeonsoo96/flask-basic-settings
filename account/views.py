from flask import request, jsonify
from flask.views import MethodView
from settings.serialize import serialize
from .models import User, db


class AccountUser(MethodView):
    def get(self):
        get_user = db.session.query(User).filter(User.user_id == request.form['user_id']).first()
        print(get_user)
        return jsonify(serialize(get_user))

    def post(self):
        try:
            new_user = User(user_id=request.form['user_id'],
                            user_pw=request.form['user_pw'],
                            user_name=request.form['user_name'])
            db.session.add(new_user)
            db.session.commit()
        except:
            return jsonify(), 400

        return jsonify(serialize(new_user)), 200

    def delete(self):
        return 'delete'

    def put(self):
        return 'put'
