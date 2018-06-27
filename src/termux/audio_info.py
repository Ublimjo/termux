#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
from box import Box

try:
    from sh import termux_audio_info
except ImportError:
    print('Unable to find termux_audio_info')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class audio_info:
    """
    Get information about audio capabilities.
    """
    def __init__(self):
        self.output = termux_audio_info()
        self.result = Box.from_json(str(self.output))


    def __getitem__(self, key):
        return self.result[key]


    def __str__(self):
        return str(self.result)


    def __reprr__(self):
        return repr(self.result)
