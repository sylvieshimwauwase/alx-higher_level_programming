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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs == [] or None:
                json.dump(list_objs, filename)
            else:
                j_str = cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                        )
                f.write(j_str)
