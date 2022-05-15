import pymongo
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://admin:admin@localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    print("DataBase Created")
    return client['iot']


def get_table(db,table):
    return db[table]

db = get_database()
table = get_table(db,"bat1charge")

table.insertOne({"ola":"adeus"})
