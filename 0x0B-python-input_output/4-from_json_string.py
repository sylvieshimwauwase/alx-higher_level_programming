#!/usr/bin/python3
"""json string to objects"""
import json


def from_json_string(my_str):
    """returning an object represented by json"""

    return json.loads(my_str)
