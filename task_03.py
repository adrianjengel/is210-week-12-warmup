#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Defining a custom logger."""

    def __init__(self, logfilename):
        """Initializing function."""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """A custom log."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """A flush fuction."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except self.log(Exception):
            raise Exception
        try:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
                except self.log(IOError):
                    break
        except self.log(Exception):
            pass
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
