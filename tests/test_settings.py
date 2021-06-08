#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import settings
import os


def test_config():
    assert(settings.settings_dict['logfile'] == '../log/info.log')


def test_load_json():
    settings_dict = settings.load_json('../config/settings.json')
    assert(settings_dict['logfile'] == '../log/info.log')


def test_logfile():
    assert(settings.logfile == '../log/info.log')


def test_build_path():
    actual = settings._build_path('../config/settings.json')

    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(dir, '../config/settings.json'))
    assert(path == actual)


def test_notfilepath_json():
    try:
        settings.load_json('../config/settings.jso')
    except FileNotFoundError as e:
        assert(str(e) == '/data/config/settings.jso')
