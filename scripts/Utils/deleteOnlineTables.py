import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017/"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client['iot']
mycol = db['onlineBat01']
mycol.drop()
mycol2 = db['onlineBat02']
mycol2.drop()