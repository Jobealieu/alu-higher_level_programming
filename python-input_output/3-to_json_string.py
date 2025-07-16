#!/usr/bin/env python3
"""Module that converts Python objects to JSON strings"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    
    Args:
        my_obj: The Python object to convert to JSON string
        
    Returns:
        str: JSON string representation of the object
    """
    return json.dumps(my_obj)
