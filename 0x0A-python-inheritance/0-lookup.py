#!/usr/bin/python3
def lookup(obj):
    """function to return list of available attributes"""

    attr = dir(obj)
    return attr
