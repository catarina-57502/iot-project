import json
from pymongo import MongoClient

FILE = '../datasets/online_1/offline_.json'


def writeCSVtoDB(File,tableDB):


    file = open(File, 'r',encoding="utf8")
    data = json.load(file)
    for i in data:
        data[i]["_id"] = i
        print(data[i])
        tableDB.insert_one(data[i])
    file.close()
    print("DONE", File)


def get_database():
    CONNECTION_STRING = "mongodb+srv://admin:admin@iot.qwwov.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    print("DataBase Created")
    return client['iot']


def get_table(db,table):
    print("Table:",table,"created!")
    return db[table]


if __name__ == "__main__":
    db = get_database()
    dbTable = get_table(db,'offline')
    writeCSVtoDB(FILE,dbTable)