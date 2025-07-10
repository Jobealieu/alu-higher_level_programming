#!/usr/bin/python3
"""Module defining LockedClass"""


class LockedClass:
    """Prevents dynamic attribute creation except first_name"""
    __slots__ = ['first_name']
