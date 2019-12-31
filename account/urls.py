from flask import Blueprint

app = Blueprint('account', __name__)

@app.route('/')
def account():
    # todo make account func
    return 'asd'