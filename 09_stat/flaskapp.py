#Benjamin Avrahami
#SoftDev1 pd 2
#
#2019-09-19


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "hablo queso!"

@app.route("/index")
def dummy():
    return "You are at the index"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def next():
    return render_template('fib.html',val=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
