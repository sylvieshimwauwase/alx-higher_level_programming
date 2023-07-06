#!/usr/bin/python3
from typing import Any


class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError("Cannot create new instance attribute")
        super().__setattr__(name, value)
