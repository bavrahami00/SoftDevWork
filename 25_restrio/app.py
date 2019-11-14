#Benjamin Avrahami, Tyler Huang
#SoftDev1 pd2
#K25 -- Getting More REST
#2019-11-12

from flask import Flask
from flask import render_template
import urllib
import json
import urllib3
app = Flask(__name__)

@app.route("/map")
def geo():
    u = urllib.request.urlopen("http://open.mapquestapi.com/geocoding/v1/address?key=KHiNxiOAxR7QXpKrSDHZ3sGXP65Ci4Mz&location=345+Chambers+St,New+York,NY,10282")
    response = u.read()
    data = json.loads(response)
    return render_template("mapapi.html", place=data['results'][0]['locations'][0]['street'], lat=data['results'][0]['locations'][0]['latLng']['lat'], long=data['results'][0]['locations'][0]['latLng']['lng'])

@app.route("/trivia")
def questions():
    u = urllib.request.urlopen("https://opentdb.com/api.php?amount=10")
    response = u.read()
    data = json.loads(response)
    return render_template("triviaapi.html", questions=data['results'])

@app.route("/language")
def cards():
    u = http.request('POST', "http://api.languagelayer.com/detect?access_key=d9f2c4b603267e9120953a589fdc231b&query=Mr%20et%20Mrs%20Dursley,%20qui%20habitaient%20au%204,%20Privet%20Drive,%20avaient%20toujours%20affirm%C3%A9%20avec%20la%20plus%20grande%20fiert%C3%A9%20qu%27ils%20%C3%A9taient%20parfaitement%20normaux,%20merci%20pour%20eux.")
    reponse = u.read()
    data = json.loads(response)
    return render_template("languageapi.html", name=data['results'][0]['language_name'], prob=data['results'][0]['probability'])

if __name__ == "__main__":
    app.debug = True
    app.run()
