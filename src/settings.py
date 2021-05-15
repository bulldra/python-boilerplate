#!/usr/bin/env python3
__version__ = "0.1.0"

import os
import json

def load_json(path):
    path = _build_path(path)
    if path is not None:
        with open(path, 'r') as conf:
            return json.load(conf)
    else:
        return {}

def load_text(path):
    path = _build_path(path)
    if path is not None:
        result = []
        with open(path, 'r') as conf:
            for line in conf.read().splitlines():
                result.append(line)
            return result
    else:
        return []

def _build_path(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    return path if os.path.exists(path) else None

settings_dict = load_json('../config/settings.json')
# secrets_dict = load_json('../config/secrets.json')
