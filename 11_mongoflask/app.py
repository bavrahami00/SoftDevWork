from flask import Flask
from utl import ops

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "hablo queso!"

@app.route("/index")
def ind():
    return "Main page"

@app.route("/page")
def dummy():
    return "Lorem ipsum doloret"

if __name__ == "__main__":
    app.debug = True
    app.run()
