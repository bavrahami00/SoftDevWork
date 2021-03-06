#Benjamin Avrahami, William Lin
#SoftDev1 pd 2
#K10 - Jinja Tuning
#2019-09-24


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

def weight(occ):
  num = random.random() * 100
  count = 0
  for x in occ:
    count = count + float(occ[x])
    if count > num and x != "Total":
      return (x)
  return (weight(occ))



@app.route("/occupyflaskst")
def occ():
    rand = weight(ref)
    return render_template('occ.html',dict=ref,chose=rand)

if __name__ == "__main__":
    app.debug = True
    app.run()

