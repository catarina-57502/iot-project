#!/usr/bin/env python3
"""a simple sensor data generator that sends to an MQTT broker via paho"""
import sys
import json
import time
import paho.mqtt.client as mqtt
import os
import signal
import getopt
from random import seed
from random import randint
# seed random number generator
seed(1)


def signal_handler(sig, frame):
    #print('You pressed Ctrl+C.\nProgram closed.')
    sys.exit(0)


def main(argv):

    signal.signal(signal.SIGINT, signal_handler)
    
    broker = "broker.hivemq.com" 
    port = 1883
    topic = "temp"

    mqttc = mqtt.Client("Publisher")
    mqttc.connect(broker, port)
    msgs_sent = 0
    mqttc.loop_start()

    while(1):
        try:
            payload = json.dumps({"data": randint(10, 40) })
            print("Sending msg: " + payload)
            mqttc.publish(topic, payload)
            msgs_sent += 1
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()
    mqttc.loop_stop()

    print("Messages sent: " + str(msgs_sent))

if __name__ == "__main__": 
    main(sys.argv[1:])
