#!/usr/bin/env python3

import sys
import json
import time
import paho.mqtt.client as mqtt
import os
import signal
import getopt
import threading


FILEOFFLINE = "../dataSets/offline_.json"


broker = "34.152.63.25"
port = 1883

mqttc = mqtt.Client("Publisher")
mqttc.connect(broker, port)
mqttc.loop_start()

f = open(FILEOFFLINE)

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

data = json.load(f)

def Battery01(data):
    topicBat01 = "idc"

    for cycle in data:
        if(data[cycle]["battery_ID"] == "1"):
            size = len(data[cycle]["voltage_battery"])
            print(size)
            for i in range(size):
                try:
                    jso = { "battery_ID": data[cycle]["battery_ID"],
                        "cycle_number": data[cycle]["cycle_number"],
                        "type": data[cycle]["type"],
                        "amb_temp": data[cycle]["amb_temp"],
                        "date_time": data[cycle]["date_time"],
                        "voltage_battery": data[cycle]["voltage_battery"][i],
                        "current_battery": data[cycle]["current_battery"][i],
                        "temp_battery": data[cycle]["temp_battery"][i],
                        "current_load": data[cycle]["current_load"][i],
                        "voltage_load": data[cycle]["voltage_load"][i],
                        "time": data[cycle]["time"][i],
                        "elapsed_time": data[cycle]["elapsed_time"]
                    }
                    payload =  json.dumps(jso)
                    print(payload)
                    mqttc.publish(topicBat01, payload)
                    time.sleep(5)
                except KeyboardInterrupt:
                    sys.exit()


    print("Messages sent: " + str(msgs_sent))

def Battery02(data):
    topicBat02 = "idc/fc05/bat02"

    for cycle in data:
        if (data[cycle]["battery_ID"]) == "2":
            size = len(data[cycle]["voltage_battery"])
            print(size)
            for i in range(size):
                try:
                    jso = { "battery_ID": data[cycle]["battery_ID"],
                        "cycle_number": data[cycle]["cycle_number"],
                        "type": data[cycle]["type"],
                        "amb_temp": data[cycle]["amb_temp"],
                        "date_time": data[cycle]["date_time"],
                        "voltage_battery": data[cycle]["voltage_battery"][i],
                        "current_battery": data[cycle]["current_battery"][i],
                        "temp_battery": data[cycle]["temp_battery"][i],
                        "current_load": data[cycle]["current_load"][i],
                        "voltage_load": data[cycle]["voltage_load"][i],
                        "time": data[cycle]["time"][i],
                        "elapsed_time": data[cycle]["elapsed_time"]
                    }
                    payload =  json.dumps(jso)
                    print(payload)
                    mqttc.publish(topicBat02, payload)
                    time.sleep(5)
                except KeyboardInterrupt:
                    sys.exit()


    print("Messages sent: " + str(msgs_sent))

if __name__ == "__main__":
    bat01 = threading.Thread(target=Battery01, args=(data,))
    bat02 = threading.Thread(target=Battery02, args=(data,))
    bat01.start()
    bat02.start()
