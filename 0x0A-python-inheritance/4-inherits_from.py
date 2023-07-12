#!/usr/bin/python3
"""subclass inherited"""


def inherits_from(obj, a_class):
    """checks if an object is instance that inherited from"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
