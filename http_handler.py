"""
HTTP Handler
"""

from flask import Flask, request
from mqtt_handler import client
from config import agent_connections, max_id
import json
import re

app = Flask(__name__)
app.threaded = True


def is_valid(my_json: json):
    try:
        if not re.match(r'^[\w+\-]+$', my_json['agent_id']):
            return False
        if not re.match(r'^\d+$', my_json['thing_id']):
            return False
        if not re.match(r'^[a-zA-Z]+$', my_json['thing_type']):
            return False
        if not type(my_json['states']) is list:
            return False
    except KeyError:
        return False
    return True


@app.route('/setsetting', methods=['POST'])
def set_setting():
    """
    :returns 400, if request isn't in right format, returns 'Bad Request'
    :returns 429, if requests are more than max,
        returns 'Too Many Requests Error'
    """

    if not is_valid(request.json):
        return '400'  # Bad Request

    i = 0
    while agent_connections[i]:  # finding an empty place in array
        i = i + 1
        if i >= max_id:
            return '429'  # Too Many Requests

    agent_connections[i] = True

    req = request.json
    req['id'] = i  # setting an id to the request
    client.publish('agent', json.dumps(req))  # publishing the request for MQTT

    agent_connections[i] = False

    return 'Done'


@app.errorhandler(404)
def page_not_found():
    """
    :returns 404, if request's url isn't valid, returns 'Bad Request'
    """

    return '404'  # Page Not Found
