import json

from pymongo import MongoClient
client = MongoClient()
db = client["restaurants"]
col = db["inventory"]

data = {}
with open('primer-dataset.json','r') as f:
    data = f.read().replace("$date", "date")
    col.insert_many(data)

#def find_by_borough(bor):
    #print()
