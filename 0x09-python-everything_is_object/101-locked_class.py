#!/usr/bin/python3
from typing import Any


class LockedClass:
    """
    preventing from instantiating new LockedClass
    """
    __slots__ = ['first_name']
