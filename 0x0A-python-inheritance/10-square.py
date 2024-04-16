#!/usr/bin/python3
"""Square a subclass of rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """init a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate are if square"""
        return self.__size ** 2
    

