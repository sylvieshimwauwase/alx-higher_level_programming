#!/usr/bin/python3
"""Searching and updating text line"""


def append_after(filename="", search_string="", new_string=""):
    """inserting a line of texts to a file """

    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
