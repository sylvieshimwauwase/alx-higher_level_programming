#!/usr/bin/python3
"""writing a file"""


def write_file(filename="", text=""):
    """writes utf-8 file and returns number of characters written"""

    with open(filename, encoding="utf-8") as file:
        for char in file:
            print(file.write(text), end="")
