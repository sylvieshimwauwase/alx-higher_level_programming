#!/usr/bin/python3
"""reading file"""


def read_file(filename=""):
    """read utf-8 file and print its content to stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
