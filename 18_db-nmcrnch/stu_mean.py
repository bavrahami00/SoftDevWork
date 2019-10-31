#Benjamin Avrahami
#SoftDev  Pd 2
#K17 :: Average 
#Oct 11, 2019

import sqlite3
import csv

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()


numbers = {}
totals = {}
ids = {}

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
foo = c.execute(q)
for bar in foo:
  if bar[0] in numbers:
    numbers[bar[0]] += 1
    totals[bar[0]] += bar[2]
  else:
    numbers[bar[0]] = 1
    ids[bar[0]] = bar[1]
    totals[bar[0]] = bar[2]

c.execute("CREATE TABLE stu_avg (id INTEGER, average NUMERIC);")

for man in ids:
  av = totals[man] / numbers[man]
  print ("name = " + man + ", id = " + str(ids[man]) + ", average = " + str(av))
  command = "INSERT INTO stu_avg VALUES (" + str(ids[man]) + ", " + str(av) + ");"
  c.execute(command)

db.commit()
db.close()
