from flask import Flask, render_template
import csv
import random
app = Flask(__name__)


file = "occupations.csv"
ref = {}
with open(file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  go = False
  for row in reader:
    if go:
      ref[row[0]] = row[1]
    else:
      go = True


@app.route("/occupyflaskst")

def hello_world():
    return render_template('occ.html',dict=ref)

if __name__ == "__main__":
    app.debug = True
    app.run()

