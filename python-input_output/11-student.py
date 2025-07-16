#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student instance

        Args:
            attrs: List of attribute names to retrieve, or None for all

        Returns:
            Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """Replace all attributes of Student instance from dictionary

        Args:
            json: Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
