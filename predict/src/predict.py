import time
import requests
import random
import datetime
import json
import os
import paho.mqtt.client as mqtt
 
broker_address = os.getenv('MQTT_HOST')
dev_topic = os.getenv('MQTT_DEV_TOPIC')
pred_topic = os.getenv('MQTT_PREDICT_TOPIC')
scoring_url=os.getenv('SCORING_URL')
d={}

client = mqtt.Client("pdm")
client.connect(broker_address)

def on_message(mosq, obj, msg):
    rotation=json.loads(msg.payload)["rotation"]
    temperature=json.loads(msg.payload)["temperature"]
    vibration=json.loads(msg.payload)["vibration"]
    sound=json.loads(msg.payload)["sound"]
    telemetry=[rotation,temperature,vibration,sound]
    data={"params":telemetry}
    
    response = requests.post(scoring_url, json=data)
    fault=json.loads(response.text)["fault"]

    d["deviceID"]=json.loads(msg.payload)["deviceID"]
    d["fault"]=fault

    payload = json.dumps(d, ensure_ascii=False)
    print(payload)
    client.publish(pred_topic,payload)
    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect(broker_address)
client.subscribe(dev_topic, 0)

while True:
    client.loop()