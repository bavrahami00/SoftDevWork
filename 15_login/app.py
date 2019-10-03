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
    print(__name__)
    session["user"] = "Gold"
    session["pass"] = "Potatoes"
    print (session)
    return render_template('loginpage.html')

@app.route("/auth")
def verify():
    session["username"] = request.cookies.get("username")
    session["password"] = request.cookies.get("password")
    print (session["user"])
    print (session["pass"])
    print (session["username"])
    print (session["password"])
    print (request.cookies.get("username"))
    print (request.cookies.get("password"))
    print (request.args["username"])
    print (request.args["password"])
    if session["user"] == session["username"] and session["pass"] == session["password"]:
        return redirect(url_for(welcome()))
    else:
        return "No"

@app.route("/home")
def welcome():
    print ("Welcome")

if __name__ == "__main__":
    app.debug = True
    app.run()
