#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Rewrite shebangs in specified files for running under Termux,
which is done by rewriting #!*/bin/binary to #!$PREFIX/bin/binary.
'''

from __future__ import division, print_function, absolute_import

import sys
from sh import ErrorReturnCode_2

try:
    from sh import termux_fix_shebang
except ImportError:
    print('Unable to find termux_fix_shebang')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


def fix_shebang(path):
    """
    Rewrite shebangs in specified files for running under Termux,
    which is done by rewriting #!*/bin/binary to #!$PREFIX/bin/binary.

    :param path: path of the file to fix
    :type path: str
    """
    try:
        termux_fix_shebang(path)
    except ErrorReturnCode_2 as e:
        print(e.stderr)
