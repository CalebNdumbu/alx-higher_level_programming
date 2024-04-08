#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle class
        Args:
            width: represent the width of the rectangle
            height: represent height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return((self.__width * 2) + (self.__height * 2))
