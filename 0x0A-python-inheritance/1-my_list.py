#!/usr/bin/python3
""" class Mylist that inherits from List"""


class MyList(list):
    """sub class"""

    def print_sorted(self):
        """printing sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
