#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description in the format [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
