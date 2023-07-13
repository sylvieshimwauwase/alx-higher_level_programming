#!/usr/bin/python3
"""creating object from json file"""
import json


def load_from_json_file(filename):
    """function that creates an object from json file"""

    with open(filename) as file:
        json.loads(file)
