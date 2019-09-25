from flask import Flask, render_template
app = Flask(__name__)


@app.route("/foo.html")

def hello_world():
    print(app)
    return render_template("page.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
