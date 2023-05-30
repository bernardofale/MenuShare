import json
import paho.mqtt.client as mqtt
import threading
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("vanetza/out/vam")

# É chamada automaticamente sempre que recebe uma mensagem nos tópicos subscritos em cima
def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode('utf-8'))

    print('Topic: ' + str(msg.topic))
    print('Message' + str(message))

    # lat = message["latitude"]
    # ...


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.98.20", 1883, 60)  # vru 1

threading.Thread(target=client.loop_forever).start()

