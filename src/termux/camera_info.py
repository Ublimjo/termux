#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
from box import Box
from termux import Termux_object

try:
    from sh import termux_camera_info
except ImportError:
    print('Unable to find termux_audio_info')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class camera_info(Termux_object):
    """
    Get information about device camera(s).
    """
    def __init__(self):
        self.output = termux_camera_info()
        self.result = Box.from_json(str(self.output))
