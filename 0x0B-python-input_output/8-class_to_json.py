#!/usr/bin/python3
"""Classes with Json"""


def class_to_json(obj):
    """function that returns dictionary description"""

    attrib = obj.__dict__
    json_dict = {}

    for key, value in attrib.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
