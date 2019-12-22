from flask import Flask

#define
HOST_ADDR = '0.0.0.0'
PORT_NUM = '8080'


app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(host=HOST_ADDR, port=PORT_NUM, debug=True)