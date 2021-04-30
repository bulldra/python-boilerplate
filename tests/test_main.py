#!/usr/bin/env python3
__version__ = "0.1.0"

import pytest
import main

def test_answer():
    assert main.Main().execute() == True
