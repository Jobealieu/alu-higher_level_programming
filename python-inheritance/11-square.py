# 11-square.py

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
