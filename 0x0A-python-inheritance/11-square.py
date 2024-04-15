#!/usr/bin/python3
"""Square a subclass of rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """init a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return  string representation of square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
    
    def area(self):
        """Calculate area"""
        return self.__size ** 2