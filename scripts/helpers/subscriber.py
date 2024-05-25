# python3.6

from paho.mqtt import client as mqtt_client
from helpers.config import settings
import uuid
import os
import json
import random


MQTT_BROKER_HOST = 'host.docker.internal'
MQTT_BROKER_PORT = settings.MQTT_BROKER_PORT
MQTT_BROKER_USER = settings.MQTT_BROKER_USER
MQTT_BROKER_PASS = settings.MQTT_BROKER_PASS
MQTT_MAIN_TOPIC  =  settings.MQTT_MAIN_TOPIC

client_id = f'subscribe-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(MQTT_BROKER_USER, MQTT_BROKER_PASS)
    
    client.on_connect = on_connect
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)
    return client

def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        handler(json.loads(msg.payload.decode('utf-8')))

    client.subscribe(topic)
    client.on_message = on_message

def run(topic):
    client = connect_mqtt()
    subscribe(client, topic)
    client.loop_forever()
    
def handler(payload):
    print(payload)

