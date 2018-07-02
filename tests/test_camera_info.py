#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from termux import camera_info

__author__ = "Ublim"
__copyright__ = "Ublim"
__license__ = "mit"


workon = camera_info()


def test_id():
    assert workon[0]['id'] == 0
