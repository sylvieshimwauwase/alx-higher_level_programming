#!/usr/bin/python3
"""writing a file"""


def write_file(filename="", text=""):
    """writes utf-8 file and returns number of characters written"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
