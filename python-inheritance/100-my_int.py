#!/usr/bin/python3
"""
MyInt class that inherits from int with inverted == and != operators
"""


class MyInt(int):
    """A rebel integer class with inverted equality operators"""

    def __eq__(self, other):
        """Override equality operator to return inverted result"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override not-equal operator to return inverted result"""
        return super().__eq__(other)
