import csv
import random

fil = "occupations.csv"

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
