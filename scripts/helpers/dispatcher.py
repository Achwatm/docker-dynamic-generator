from helpers.config import settings
import time
import random
import gzip
from paho.mqtt import client as mqtt_client
import paho.mqtt.publish as publish
import json
from helpers.job import Job
import uuid


MQTT_BROKER_HOST = settings.MQTT_BROKER_HOST
MQTT_BROKER_PORT = settings.MQTT_BROKER_PORT
MQTT_BROKER_USER = settings.MQTT_BROKER_USER
MQTT_BROKER_PASS = settings.MQTT_BROKER_PASS
MQTT_MAIN_TOPIC  =  settings.MQTT_MAIN_TOPIC


response={
    'data': None,
    'exec_time': 0,
    'transaction_id': None
}
client_id = f'publish-{random.randint(0, 1000)}'

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

def publish(client, topic, job_payload):
    msg_count = 1
    while True:
        time.sleep(1)
        result = client.publish(topic, job_payload)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{job_payload}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

def run(user):
    startTime = time.time()
    
    job = Job()
    job.add_topic('observer_'+user)
    
    client = connect_mqtt()
    client.loop_start()
    publish(client, 'observer_'+user, job.dump())
    client.loop_stop()
    startTime = time.time()
    
    # create job
    executionTime = (time.time() - startTime)

    print("\n---> Execution time in seconds: " + str(executionTime))

    return True
