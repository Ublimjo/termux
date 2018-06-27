#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
from box import Box
from termux import Termux_object

try:
    from sh import termux_battery_status
except ImportError:
    print('Unable to find termux_audio_info')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class battery_status(Termux_object):
    """
    Get the status of the device battery.
    """
    def __init__(self):
        self.output = termux_battery_status()
        self.result = Box.from_json(str(self.output))
