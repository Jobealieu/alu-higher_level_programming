#!/usr/bin/python3
"""Module defining LockedClass"""


class LockedClass:
    """A class that prevents dynamic creation of instance attributes
    except for 'first_name'"""
    
    __slots__ = ['first_name']
