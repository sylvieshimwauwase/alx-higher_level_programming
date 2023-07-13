#!/usr/bin/python3
"""Class students to Json"""


class Student:
    """defining class students"""

    def __init__(self, first_name, last_name, age):
        """
        Initializing student instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieving dictionary representation
        """

        if attrs is None:
            return self.__dict__

    json_dict = {}

    for attr in attrs:
        if hasattr(self, attr):
            json_dict[attr] = getattr(self, attr)

    return json_dict
