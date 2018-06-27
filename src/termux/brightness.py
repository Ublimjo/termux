#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
from box import Box

try:
    from sh import termux_brightness
except ImportError:
    print('Unable to find termux_audio_info')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


def brightness(n):
    """
    Set the screen brightness between 0 and 255

    :param n: value of brightness between 0 and 255
    :type n: int
    """

    n = int(n)
    if 0 <= n <= 255:
        termux_brightness(n)
    else:
        raise ValueError('Value must be between 0 and 255')
