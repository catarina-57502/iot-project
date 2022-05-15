import json
from pymongo import MongoClient

FILE = 'offline_.json'


def writeCSVtoDB(File,tableDBat1Charge,tableDBat1Dis,tableDBat2Charge,tableDBat2Dis):


    file = open(File, 'r',encoding="utf8")
    data = json.load(file)
    for i in data:
        data[i]["_id"] = i
        print(data[i]["_id"])
        if(data[i]["battery_ID"] == "1"):
            if (data[i]["type"] == "charge"):
                tableDBat1Charge.insert_one(data[i])
            if (data[i]["type"] == "discharge"):
                tableDBat1Dis.insert_one(data[i])
        if(data[i]["battery_ID"] == "2"):
            if (data[i]["type"] == "charge"):
                tableDBat2Charge.insert_one(data[i])
            if (data[i]["type"] == "discharge"):
                tableDBat2Dis.insert_one(data[i])

    file.close()
    print("DONE", File)


def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    print("DataBase Created")
    return client['iot']


def get_table(db,table):
    print("Table:",table,"created!")
    return db[table]


if __name__ == "__main__":
    db = get_database()
    dbTable1c = get_table(db,'bat1charge')
    dbTable2c = get_table(db,'bat2charge')
    dbTable1d = get_table(db,'bat1discharge')
    dbTable2d = get_table(db,'bat2discharge')
    writeCSVtoDB(FILE,dbTable1c,dbTable1d,dbTable2c,dbTable2d)