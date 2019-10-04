#David "Snake" Wang and Benjamin Avrahami
#SoftDev1 pd2
#K15: Do I Know You?
#2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for
from utl import key
app = Flask(__name__) #create instance of class Flask

app.secret_key = key.get_key()


@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    session["username"] = "Gold"
    session["password"] = "Potatoes"
    if "user" in session:
        if session["user"] == session["username"] and session["pass"] == session["password"]:
            return redirect(url_for("welcome")) 
    return redirect(url_for("log"))

@app.route("/login")
def log():
    return render_template('loginpage.html')

@app.route("/logout")
def ex():
    session.pop("user")
    session.pop("pass")
    return redirect(url_for("log"))

@app.route("/auth")
def verify():
    #session["username"] = "Gold"
    #session["password"] = "Potatoes"
    session["user"] = request.args["username"]
    session["pass"] = request.args["password"]
    if session["user"] == session["username"] and session["pass"] == session["password"]:
        return redirect(url_for("welcome"))
    else:
        return "No"

@app.route("/home")
def welcome():
    return render_template("well.html",u=session["user"])


if __name__ == "__main__":
    app.debug = True
    app.run()
