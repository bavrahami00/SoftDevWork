#benjamin Avrahami
#SoftDev  Pd 2
#K17 :: SQLITE3 BASICS
#Oct 10, 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#courses table
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

with open("data/courses.csv", 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #put in values for the table: code, mark, id
    command = "INSERT INTO courses VALUES ('" + row["code"] + "', " + row["mark"] + ", " + row["id"] + ")"
    c.execute(command)


#==========================================================
#students table
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)")

with open("data/students.csv", 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #put in values for the table: name, age, id
    command = "INSERT INTO students VALUES ('" + row["name"] + "', " + row["age"] + ", " + row["id"] + ")"
    c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database
