#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import getopt
import time
import sys
import json

def usage():
    print ("python mqttsubs -b <broker address> -p <port> -t <topic>")

def on_message(client, userdata, message):

    print("MESSAGE RECEIVED: ")
    payload = str(message.payload.decode("utf-8"))
    print(payload)
    print("")

def main(argv):

    broker = "broker.hivemq.com" 
    topic = "temp_out"
    port = 1883

    timeout = 300
    msgs_received = 0

    try:
        opts, args = getopt.getopt(argv, "h:b:p:t:f:", ["broker=", "port=", "topic=", "finish"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-b", "--broker"):
            broker = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-t", "--topic"):
            topic = arg
        elif opt in ("-f", "--finish"):
            timeout = int(arg)

    client = mqtt.Client("subscriber")
    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    start = time.time()
    elapsed = 0

    print("Subscribed, now waiting for messages ...")

    while elapsed != timeout:
        try:
            elapsed = int(time.time() - start)
            client.loop()
        except KeyboardInterrupt:
            sys.exit()
    client.loop_stop()
        
if __name__ == "__main__": 
    main(sys.argv[1:])
