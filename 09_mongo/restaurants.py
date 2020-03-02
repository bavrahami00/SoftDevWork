import json

from bson.json_util import loads

from pymongo import MongoClient
client = MongoClient()
db = client["restaurants"]
col = db["inventory"]

def ingest(f):
    fmt = ''
    with open('primer-dataset.json') as _f:
        return loads(f'[{",".join(map(lambda s: s[:len(s) - 1], _f))}]')

with open('primer-dataset.json','r') as f:
    data = ingest(f)
    col.insert_many(data)

def find_by_borough(bor):
    for store in col.find({"borough" : bor}):
        pprint.pprint(store["name"])

def find_by_zip(zip):
    for store in col.find({"address.zipcode" : zip}):
        print(store["name"])

def find_by_zip_grade(zip,grade):
    for store in col.find({"grades" : {"$elemMatch" : {"grade" : grade}}, "address.zipcode": zip}):
        print(store["name"])

def find_by_zip_score(zip,score):
    for store in col.find({"address.zipcode" : zip, "grades" : {"$elemMatch" : {"score" : {"$lt" : score}}}}):
        print(store["name"])

#find_by_borough("Manhattan")
#find_by_zip("10282")
#find_by_zip_grade("10282","A")
#find_by_zip_score("10025",12)
