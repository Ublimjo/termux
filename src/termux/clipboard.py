#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
(Get or Set) the system clipboard text.
'''

from __future__ import division, print_function, absolute_import

import sys

try:
    from sh import termux_clipboard_get
    from sh import termux_clipboard_set
except ImportError:
    print('Unable to find termux_clipboard')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


class Clipboard:
    """
    (Get or Set) the system clipboard text.
    """
    def __init__(self):
        self.memory = termux_clipboard_get() or ''

    def get(self):
        '''
        Get the system clipboard text.
        '''
        self.memory = termux_clipboard_get() or ''
        return self.memory

    def set(self, text):
        '''
        Set the system clipboard text.
        '''
        self.memory = str(text)
        termux_clipboard_set(str(text))

    def __str__(self):
        self.memory = termux_clipboard_get() or ''
        return self.memory
