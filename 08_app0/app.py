from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "hablo queso!"

@app.route("/index")
def dummy():
    return "This works"

if __name__ == "__main__":
    app.debug = True
    app.run()
