from flask import Flask
from utl import ops

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
