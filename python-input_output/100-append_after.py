#!/usr/bin/python3
"""
Module that contains the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string
    
    Args:
        filename: name of the file to modify
        search_string: string to search for in each line
        new_string: string to insert after matching lines
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
