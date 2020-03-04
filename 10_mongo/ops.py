import json
#from bson.json_util import loads

from pymongo import MongoClient
client = MongoClient()
db = client["opioids"]
col = db["inventory"]

if col.count() == 0:
    with open('ct_od_deaths.json','r') as file:
        data = json.load(file)
#        print(type(data["meta"]))
#        print(type(data["data"]))
        col.insert_one(data)
#        col.insert_many(data["data"])

#print(col.find({"meta.view.id" : "rybz-nyjw"}, {"data.0.0": 1}))
for i in col.find({"meta.view.id" : "rybz-nyjw"}, {"_id": 0, "data.0.0": 1}):
    cursor = i
    for j in cursor:
       print(j.0)
