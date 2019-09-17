import csv
import random

file = "occupations.csv"

ref = {}

with open(file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  reader.next()
  for row in reader:
    ref[row[0]] = row[1]
    
file.close()

def weight(occ):
  num = random() * 100
  count = 0
  for x in occ:
    count = count + occ[x]
    if count > num:
      return x
  return weight(occ)
