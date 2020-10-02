import time
import random
import datetime
import json
import os
import paho.mqtt.client as mqtt
 
broker_address = os.getenv('MQTT_HOST')
topic = os.getenv('MQTT_TOPIC')
fault = os.getenv('FAULT', '0')
deviceID = os.getenv('DEVICE_ID', '1')
client = mqtt.Client(deviceID)
client.connect(broker_address)
  
while True: 
    d={}
    d["deviceID"] = deviceID
    d["timeStamp"] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    if fault == '1':                     
        d["rotation"] = round(random.uniform(400,650),1)
        d["temperature"] = round(random.uniform(35.0,55.0),1)
        d["vibration"] = round(random.uniform(100.0,250.0),1)
        d["sound"] = round(random.uniform(45.0,60.0),1)
    else:
        d["rotation"] = round(random.uniform(500,700),1)
        d["temperature"] = round(random.uniform(35.0,45.0),1)
        d["vibration"] = round(random.uniform(100.0,200.0),1)
        d["sound"] = round(random.uniform(45.0,52.0),1)

    payload = json.dumps(d, ensure_ascii=False)
    print (payload)
    client.publish(topic,payload)
    time.sleep(2)