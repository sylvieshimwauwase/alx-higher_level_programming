#!/usr/bin/python3
"""creating Base class"""
import json


class Base:
    """representing Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base init
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Method that returns json string representation
        Args:
            list_dictionaries(dict): list of dictionaries
        Return:
            JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

