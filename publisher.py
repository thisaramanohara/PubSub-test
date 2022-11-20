import paho.mqtt.client as mqtt
import random
import time
import json
import datetime

mqttBroker = "mqtt.eclipseprojects.io"
client =mqtt.Client("publisher")

topic = "/3yp/ldr01/coordinates"

while True:
    client.connect("mqtt.eclipseprojects.io", port=1883)
    x = {
        "data": "Thisara"
    }

    client.publish(topic, json.dumps(x))
    print("published " + str(x) + " to topic " + topic)
    time.sleep(5)

