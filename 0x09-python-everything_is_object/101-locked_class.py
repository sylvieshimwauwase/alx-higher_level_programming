#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    preventing from instantiating new LockedClass
    """
    __slots__ = ['first_name']
