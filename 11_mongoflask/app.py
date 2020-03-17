from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from utl import ops

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return redirect(url_for("home"))

@app.route("/home")
def home():
    ops.setup()
    druglist = ops.all_drugs()
    dlist = []
    if len(request.args) > 0:
        dlist = request.args.getlist("drugs")
    dstr = ops.d_string(dlist)
    gdict = ops.gender_deaths(dlist)
    adict = ops.age_deaths(dlist)
    adict["Unrecorded"] = adict.pop(None)
    rdict = ops.race_deaths(dlist)
    rdict["Unrecorded"] = rdict.pop(None)
    return render_template("main.html",drugs=druglist,dstring=dstr,gender=gdict,age=adict,race=rdict)

if __name__ == "__main__":
    app.debug = True
    app.run()
