#!/usr/bin/env python3

import sys
import json
import time
import paho.mqtt.client as mqtt
import os
import signal
import getopt
import threading


FILEBAT01 = "../db/online_1.json"
FILEBAT02 = "../db/online_2.json"


broker = "35.203.121.245"
port = 1883
mqttc = mqtt.Client("Publisher")

mqttc.connect(broker, port)
mqttc.loop_start()


def signal_handler(sig, frame):
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
def Battery01():
    f = open(FILEBAT01)
    data = json.load(f)
    topicBat01 = "idc/bat01"
    for cycle in data:
        size = len(data[cycle]["voltage_battery"])
        for i in range(size):
            try:
                jso = { "battery_ID": data[cycle]["battery_ID"],
                    "cycle_number": cycle,
                    "type": data[cycle]["type"],
                    "voltage_battery": data[cycle]["voltage_battery"][i],
                    "current_battery": data[cycle]["current_battery"][i],
                    "temp_battery": data[cycle]["temp_battery"][i],
                    "current_load": data[cycle]["current_load"][i],
                    "voltage_load": data[cycle]["voltage_load"][i]
                }
                payload =  json.dumps(jso)
                print(payload)
                mqttc.publish(topicBat01, payload)
                time.sleep(5)
            except KeyboardInterrupt:
                sys.exit()

def Battery02():
    f = open(FILEBAT02)
    data = json.load(f)
    topicBat01 = "idc/bat02"
    for cycle in data:
        size = len(data[cycle]["voltage_battery"])
        for i in range(size):
            try:
                jso = { "battery_ID": data[cycle]["battery_ID"],
                    "cycle_number": cycle,
                    "type": data[cycle]["type"],
                    "voltage_battery": data[cycle]["voltage_battery"][i],
                    "current_battery": data[cycle]["current_battery"][i],
                    "temp_battery": data[cycle]["temp_battery"][i],
                    "current_load": data[cycle]["current_load"][i],
                    "voltage_load": data[cycle]["voltage_load"][i]
                }
                payload =  json.dumps(jso)
                print(payload)
                mqttc.publish(topicBat01, payload)
                time.sleep(7)
            except KeyboardInterrupt:
                sys.exit()

if __name__ == "__main__":
    bat01 = threading.Thread(target=Battery01, args=())
    bat02 = threading.Thread(target=Battery02, args=())
    bat01.start()
    bat02.start()
