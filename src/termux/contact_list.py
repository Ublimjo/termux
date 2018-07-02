#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
List all contacts.
'''

from __future__ import division, print_function, absolute_import

import sys
from box import Box
from termux import Termux_object

try:
    from sh import termux_contact_list
except ImportError:
    print('Unable to find termux_contact_list')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class Contact_list(Termux_object):
    """
    List all contacts.
    """
    def __init__(self):
        self.output = termux_contact_list()
        self.result = Box.from_json(str(self.output))
