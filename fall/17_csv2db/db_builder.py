#Benjamin Avrahami
#SoftDev  Pd 2
#K17 :: SQLITE3 BASICS
#Oct 10, 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

with open("data/courses.csv", 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    command = "INSERT INTO courses VALUES ('" + row["code"] + "', " + row["mark"] + ", " + row["id"] + ")"
    c.execute(command)


#==========================================================

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)")

with open("data/students.csv", 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    command = "INSERT INTO students VALUES ('" + row["name"] + "', " + row["age"] + ", " + row["id"] + ")"
    c.execute(command)

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
foo = c.execute(q)
for bar in foo:
    print (bar)

#==========================================================

db.commit() #save changes
db.close()  #close database
