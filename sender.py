# sender.py
import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/laptopA_to_laptopB"

client = mqtt.Client("LaptopA_Sender")
client.connect(BROKER, PORT, 60)

# Send messages in a loop
for i in range(5):
    msg = f"Hello from LaptopA! Message {i+1}"
    client.publish(TOPIC, msg)
    print(f"Sent: {msg}")
    time.sleep(2)  # wait 2 seconds between messages

client.disconnect()
