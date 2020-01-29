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


@app.route("/")
def route():
    u = urllib.request.urlopen('https://rickandmortyapi.com/api/character/')
    response = u.read()
    data = json.loads(response)
    img = data['results'][0]['image']
    img2 = data['results'][1]['image']
    u = urllib.request.urlopen('https://xkcd.com/614/info.0.json')
    response = u.read()
    data = json.loads(response)
    img3 = data['img']
    u = urllib.request.urlopen('https://www.balldontlie.io/api/v1/players')
    response = u.read()
    data = json.loads(response)
    name = data['data'][0]['first_name'] + ' ' + data['data'][0]['last_name']
    text = 'team name:' + data['data'][0]['team']['full_name']
    return render_template("index.html", pic = img, pic2 = img2, pic3 = img3, name = name, info = text)

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
def decode():
    url = 'http://api.languagelayer.com/detect?access_key=d9f2c4b603267e9120953a589fdc231b&query=Mr%20et%20Mrs%20Dursley,%20qui%20habitaient%20au%204,%20Privet%20Drive,%20avaient%20toujours%20affirm%C3%A9%20avec%20la%20plus%20grande%20fiert%C3%A9%20qu%27ils%20%C3%A9taient%20parfaitement%20normaux,%20merci%20pour%20eux.'
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url, headers=hdr)
    data = json.loads( urllib.request.urlopen(req).read())
    return render_template("languageapi.html", name=data['results'][0]['language_name'], prob=data['results'][0]['probability'])

if __name__ == "__main__":
    app.debug = True
    app.run()
