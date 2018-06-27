#not /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from termux import brightness

__author__ = "Ublim"
__copyright__ = "Ublim"
__license__ = "mit"


workon = brightness


def test_tooMuchValue():
    assert workon(255) == None
    assert workon(0) == None
    assert workon('100') == None
