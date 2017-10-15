"""
MQTT Handler
"""

import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    pass


def on_publish(client, userdata, result):
    pass


def on_connect(client, userdata, flags, rc):
    client.subscribe('set')  # we subscribe on 'set'


def on_disconnect(client, userdata, rc):
    pass


client = mqtt.Client('set')  # Defining a client named 'set'
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.on_disconnect = on_disconnect
