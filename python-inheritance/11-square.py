#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size

        Args:
            size (int): The size of the square (width and height)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of the square

        Returns:
            str: Square description in format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
