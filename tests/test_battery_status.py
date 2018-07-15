#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from termux import Battery_status

__author__ = "Ublim"
__copyright__ = "Ublim"
__license__ = "mit"


workon = Battery_status()


def test_percentage():
    assert 0 <= workon["percentage"] <= 100


def test_plugged():
    assert workon["plugged"] in ("UNPLUGGED", "PLUGGED_AC", "PLUGGED_DC")


def test_status():
    assert workon["status"] in ("DISCHARGING", "CHARGING", "FULL")
