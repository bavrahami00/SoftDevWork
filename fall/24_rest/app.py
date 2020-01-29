#Benjamin Avrahami, Peihua Huang (Team PI)
#SoftDev1 pd2
#K24 -- A RESTful Journey Skyward
#2019-11-12

from flask import Flask
from flask import render_template
import urllib, json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=KaSPKF6wwTVHdhAzFcp9iivZUrgmlz1TtxRHge2U")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic=data['url'], caption=data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
