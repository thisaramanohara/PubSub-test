

import paho.mqtt.client as mqtt
import json
import datetime

client = mqtt.Client("subscriber")

topic = "/3yp/ldr01/coordinates"

def on_message_for_topic(client, userdata, message):
    data = json.loads(message.payload)
    print(data)

client.message_callback_add(topic, on_message_for_topic)
client.connect("mqtt.eclipseprojects.io", port=1883)
client.subscribe([(topic, 0)])
client.loop_forever()
