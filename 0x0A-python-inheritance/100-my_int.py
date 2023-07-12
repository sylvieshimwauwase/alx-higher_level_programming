#!/usr/bin/python3
"""representing integer class"""


class MyInt(int):
    """inverting int operations"""
    def __eq__(self, other):
        """
        Override the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator.
        """
        return super().__eq__(other)
