#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    conf = open(path, 'r')
    return json.load(conf)

def load_text_list(path):
    result = []
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, 'r') as conf:
        for line in conf:
            result.append(line)
    return line

settings_dict = load_json_setting('../config/settings.json')
secrets_dict = load_json_setting('../config/secrets.json')
