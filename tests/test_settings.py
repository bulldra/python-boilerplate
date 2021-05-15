#!/usr/bin/env python3
__version__ = "0.1.0"

import settings

def test_config():
    assert settings.settings_dict['logfile'] == '../log/info.log'

def test_load_json():
    settings_dict = settings.load_json('../config/settings.json')
    assert settings_dict['logfile'] == '../log/info.log'

def test_load_text():
    settings_list = settings.load_text('../config/settings.json')
    assert settings_list[0] == '{'
    assert settings_list[1] == '    "logfile" : "../log/info.log"'
    assert settings_list[2] == '}'

def test_notfilepath_list():
    settings_list = settings.load_text('../config/settings.jso')
    assert settings_list == []

def test_notfilepath_json():
    settings_dict = settings.load_json('../config/settings.jso')
    assert settings_dict == {}
