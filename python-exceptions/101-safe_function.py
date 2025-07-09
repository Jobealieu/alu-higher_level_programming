#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely and handles any exceptions.
    
    Args:
        fct: The function to execute
        *args: Arguments to pass to the function
    
    Returns:
        The result of the function if successful, None if an exception occurs
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
