#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list): List of attribute names to retrieve.
                         If None, all attributes are retrieved.

        Returns:
            dict: Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict
