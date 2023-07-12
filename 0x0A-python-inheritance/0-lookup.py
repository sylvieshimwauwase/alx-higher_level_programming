#!/usr/bin/python3
"""defining object attribute and methods using lookup function"""


def lookup(obj):
    """function to return list of available attributes"""

    attr = dir(obj)
    return attr
