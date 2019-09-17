import csv

file = "occupations.csv"

ref = {}

with open(file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  reader.next()
  for row in reader:
    ref[row[0]] = row[1]
    
file.close()

