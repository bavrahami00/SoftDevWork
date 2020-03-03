import json
#from bson.json_util import loads

from pymongo import MongoClient
client = MongoClient()
db = client["opioids"]
col = db["inventory"]


with open('ct_od_deaths.json','r') as file:
    data = json.load(file)
#    print(type(data["meta"]))
#    print(type(data["data"]))
    col.insert_one(data)
#    col.insert_many(data["data"])
