#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
