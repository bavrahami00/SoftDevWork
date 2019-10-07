#David "Snake" Wang and Benjamin Avrahami
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for
from utl import key
app = Flask(__name__)

app.secret_key = key.get_key()


@app.route("/") #root route
def hello_world():
    session["username"] = "Gold" #hardcoded username
    session["password"] = "Potatoes" #hardcoded password
    if "user" in session:
        if session["user"] == session["username"] and session["pass"] == session["password"]: #checks whether correct login information is stored
            return redirect(url_for("welcome")) 
    return redirect(url_for("log"))

@app.route("/login") #login page
def log():
    return render_template('loginpage.html')

@app.route("/logout") #logout page
def ex():
    session.pop("user")
    session.pop("pass")
    return redirect(url_for("log"))

@app.route("/auth") #page to check login
def verify():
    session["user"] = request.args["username"]
    session["pass"] = request.args["password"]
    if session["user"] == session["username"] and session["pass"] == session["password"]: #checks whether the login is correct
        return redirect(url_for("welcome"))
    else:
        return render_template("error.html")

@app.route("/home") #home/welcome page
def welcome():
    return render_template("well.html",u=session["user"])


if __name__ == "__main__":
    app.debug = True
    app.run()
