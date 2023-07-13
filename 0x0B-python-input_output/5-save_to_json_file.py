#!/usr/bin/python3
"""save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """"writes an object to a textfile"""

    with open(filename, "w") as file:
        json.dump(my_obj, file)
