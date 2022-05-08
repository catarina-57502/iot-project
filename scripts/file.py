FILE = "/home/iotmartimmourao/IoTProjectGroup5/datasets/offline_.json"

f = open(FILE)


bat01Charge = 0
bat02Charge = 0

bat01DisCharge = 0
bat02DisCharge = 0

data = json.load(f)

for cycle in data:
    if(data[cycle]["battery_ID"] == "1" and data[cycle]["type"] == "charge"):
        bat01Charge = bat01Charge + 1
    if(data[cycle]["battery_ID"] == "1" and data[cycle]["type"] == "discharge"):
        bat01DisCharge = bat01DisCharge + 1
    if(data[cycle]["battery_ID"] == "2" and data[cycle]["type"] == "charge"):
        bat02Charge = bat02Charge + 1
    if(data[cycle]["battery_ID"] == "2" and data[cycle]["type"] == "discharge"):
        bat02DisCharge = bat02DisCharge + 1

msg.bat01Charge = bat01Charge
msg.bat02Charge = bat02Charge
msg.bat01DisCharge = bat01DisCharge
msg.bat02DisCharge = bat02DisCharge

return msg