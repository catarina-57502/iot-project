FILE = "/home/iotmartimmourao/IoTProjectGroup5/datasets/offline_.json"

f = open(FILE)


bat01Charge = 0


data = json.load(f)

for cycle in data:
    if(data[cycle]["battery_ID"] == "1" and data[cycle]["type"] == "charge"):
        bat01Charge = bat01Charge + 1


newMsg = { "payload": bat01Charge }
return newMsg
