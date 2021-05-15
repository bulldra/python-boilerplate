#!/usr/bin/env python3
__version__ = "0.1.0"

import main
import settings
import pandas
import logzero

logzero.logfile(
    settings.settings_dict['logfile'],
    loglevel=20, maxBytes=1e6, backupCount=3
)
logger = logzero.logger

def test_answer():
    assert main.Main().execute() == True
