import pymongo
from pymongo import MongoClient
import sys

id = sys.argv[1]
arr = id.split("|")

CONNECTION_STRING = "mongodb://localhost:27017/"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client['iot']
mycol = db['onlineBat01']

myquery = { "_id": arr[0] }

docs = mycol.find(myquery)

for i in docs:
    i["voltage_battery"].append(arr[3])
    i["current_battery"].append(arr[4])
    i["temp_battery"].append(arr[5])
    i["current_load"].append(arr[6])
    i["voltage_load"].append(arr[7])
    mycol.update_one(myquery, {"$set":i})