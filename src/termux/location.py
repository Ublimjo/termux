#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Get the device location.
'''

from __future__ import division, print_function, absolute_import

import sys
from box import Box
from termux import Termux_object

try:
    from sh import termux_location
except ImportError:
    print('Unable to find termux_location')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class Location(Termux_object):
    """
    Get the device location.

    :param provider: location provider [gps/network/passive] (default: gps)
    :type provider: str

    :param request: kind of request to make [once/last/updates] (default: once)
    :type request: str
    """
    def __init__(self, provider='gps', request='once'):
        if  provider not in ('gps', 'network', 'passive'):
            raise TypeError(
                'Provider must be (gps, network, passive) not {}'.format(
                    provider
                )
            )
        if request not in ('once', 'last', 'updates'):
            raise TypeError(
                'Request must be (once, last, updates) not {}'.format(
                    request
                )
            )
        self.output = termux_location('-p', provider, '-r', request)
        self.result = Box.from_json(str(self.output))
