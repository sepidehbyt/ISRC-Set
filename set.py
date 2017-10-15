"""
Main
"""

from http_handler import app
from mqtt_handler import client
from config import http_address, http_port, broker_address, broker_port

if __name__ == '__main__':
    client.connect(broker_address, broker_port)
    client.loop_start()
    app.run(host=http_address, port=http_port)
    client.loop_forever()
