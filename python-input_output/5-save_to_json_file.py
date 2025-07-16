#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    
    Args:
        my_obj: The object to be serialized to JSON
        filename: The name of the file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
