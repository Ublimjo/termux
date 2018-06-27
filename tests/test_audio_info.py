#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from termux import audio_info

__author__ = "Ublim"
__copyright__ = "Ublim"
__license__ = "mit"


workon = audio_info()


def test_STREAM_MUSIC_VOLUME():
    assert 0 <= workon["STREAM_MUSIC_VOLUME"] <= workon["STREAM_MUSIC_MAXVOLUME"]


def test_BLUETOOTH_A2DP_IS_ON():
    assert workon["BLUETOOTH_A2DP_IS_ON"] in (True, False)


def test_WIREDHEADSET_IS_CONNECTED():
    assert workon["WIREDHEADSET_IS_CONNECTED"] in (True, False)
