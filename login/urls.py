from flask import Blueprint

app = Blueprint('login', __name__)

@app.route('/')
def login():
    # todo make login func
    return 'asd'
