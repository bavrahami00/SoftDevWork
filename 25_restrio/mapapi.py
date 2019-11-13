#Benjamin Avrahami, Tyler Huang
#SoftDev1 pd2
#K25 -- Getting More REST
#2019-11-12

from flask import Flask
from flask import render_template
import urllib
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen("http://open.mapquestapi.com/geocoding/v1/address?key=KHiNxiOAxR7QXpKrSDHZ3sGXP65Ci4Mz&location=345+Chambers+St,New+York,NY,10282")
    response = u.read()
    data = json.loads(response)
    return render_template("mapapi.html", place=data['results'][0]['locations'][0]['street'], lat=data['results'][0]['locations'][0]['latLng']['lat'], long=data['results'][0]['locations'][0]['latLng']['lng'])

if __name__ == "__main__":
    app.debug = True
    app.run()
