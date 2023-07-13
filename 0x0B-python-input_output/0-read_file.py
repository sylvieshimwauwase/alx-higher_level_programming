#!/usr/bin/python3
"""reading file"""


def read_file(filename=""):
    """read utf-8 file and print its content to stdout"""

    if not filename:
        filename = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
