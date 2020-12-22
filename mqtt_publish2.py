import paho.mqtt.client as mqtt
from random import randrange
import time

mqttBroker ="mqtt.eclipse.org"

client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
