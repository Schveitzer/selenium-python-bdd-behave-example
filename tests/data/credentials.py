import os
import json


def load_credentials():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')) as data:
        credentials = json.load(data)
    return credentials
