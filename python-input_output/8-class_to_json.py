#!/usr/bin/python3
"""Module that contains class_to_json function"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        Dictionary containing all serializable attributes of the object
    """
    return obj.__dict__
