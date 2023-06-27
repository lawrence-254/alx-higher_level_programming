#!/usr/bin/python3

class Square:
    """Class representing a square"""

    @property
    def size(self):
        """Getter method for retrieving the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size * self.__size

