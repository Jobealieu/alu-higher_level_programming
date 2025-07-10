#!/usr/bin/python3
"""
Module that defines a function to add attributes to objects
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible

    Args:
        obj: The object to add the attribute to
        attr: The attribute name
        value: The attribute value

    Raises:
        TypeError: If the object can't have new attributes
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
        return

    if hasattr(obj, '__slots__'):
        if attr in obj.__slots__:
            setattr(obj, attr, value)
            return

    raise TypeError("can't add new attribute")
