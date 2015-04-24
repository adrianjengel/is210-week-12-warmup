#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Defining a custom error class."""
    pass


def get_age(birthyear):
    """A function to test the age."""
    age = datetime.datetime.now().year - birthyear
    if not age > 0:
        raise InvalidAgeError()
    return age
