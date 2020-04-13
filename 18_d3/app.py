import csv

from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

def ops():
	with open('school_scores.csv') as file:
		reader = csv.reader(file,delimiter=',')
		ans = []
		states = {}
		state = "Alaska"
		scores = {}
		for row in reader:
			if row[0] != "Year":
				if row[2] == state:
					scores[row[0]] = int(row[3])+int(row[5])
				else:
					states[state] = scores
					scores = {}
					state = row[2]
					scores[row[0]] = int(row[3])+int(row[5])
		states[state] = scores
		return states
	return 0



@app.route("/")
def hello_world():
	states = ops()
	return render_template("home.html",scores=states)


if __name__ == "__main__":
    app.debug = True
    app.run()