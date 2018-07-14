#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Set the screen brightness
'''

from __future__ import division, print_function, absolute_import

import sys

try:
    from sh import termux_download
except ImportError:
    print('Unable to find termux_download')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


def download(url, desc='', title=''):
    """
    Download a resource using the system download manager.

    :param url: url to download
    :type url: str

    :param desc: description for the download request notification
    :type desc: str

    :param title: title for the download request notification
    :type title: str
    """

    termux_download(
            url,
            desc if desc,
            title if title,
    )
