import paho.mqtt.client as mqtt
import random
import time

# Define MQTT broker
broker_address = "mqtt.eclipseprojects.io"
client = mqtt.Client("LinodeEdgeNode")
client.connect(broker_address)


while True:
    temperature = round(random.uniform(20.0, 30.0), 2)
    client.publish("sensor/temperature", str(temperature))
    print(f"Published Temperature: {temperature}°C")
    time.sleep(5)

if temperature > 28.0:
    client.publish("sensor/alerts", f"High Temperature Alert: {temperature}°C")
