#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from termux import Location

__author__ = "Ublim"
__copyright__ = "Ublim"
__license__ = "mit"


workon = Location()


def test_latitude():
    assert -180 <= workon["latitude"] <= 180


def test_longitude():
    assert -180 <= workon["longitude"] <= 180


def test_provider():
    assert workon["provider"] in ('gps', 'network', 'passive')
