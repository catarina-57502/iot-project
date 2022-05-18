import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017/"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client['iot']
mycol = db['onlineBat01']
a = mycol.find()

for i in a:
    print(i)