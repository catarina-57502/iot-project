#!/usr/bin/env python3
"""a simple sensor data generator that sends to an MQTT broker via paho"""
import sys
import json
import time
import paho.mqtt.client as mqtt
import os
import signal
import getopt


dataset = [{"data": [{"value": 5.4},{"value": 3.4},{"value": 1.7},{"value": 0.2}]}, #Iris-setosa
           {"data": [{"value": 5.0},{"value": 3.5},{"value": 1.6},{"value": 0.6}]}, #Iris-setosa
           {"data": [{"value": 5.5},{"value": 2.4},{"value": 3.8},{"value": 1.1}]}, #Iris-versicolor
           {"data": [{"value": 5.7},{"value": 3.0},{"value": 4.2},{"value": 1.2}]}, #1Iris-versicolor
           {"data": [{"value": 7.3},{"value": 2.9},{"value": 6.3},{"value": 1.8}]}, #Iris-virginica
           {"data": [{"value": 6.0},{"value": 3.0},{"value": 4.8},{"value": 1.8}]}, #Iris-virginica
]


def signal_handler(sig, frame):
    #print('You pressed Ctrl+C.\nProgram closed.')
    sys.exit(0)


def main(argv):

    signal.signal(signal.SIGINT, signal_handler)
    
    broker = "broker.hivemq.com" 
    port = 1883
    topic = "classification"

    num_msgs_send = len(dataset)

    mqttc = mqtt.Client("Publisher")
    mqttc.connect(broker, port)
    msgs_sent = 0
    mqttc.loop_start()

    for i in range(num_msgs_send):
        try:
            payload = json.dumps(dataset[i])
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
