#!/usr/bin/python3
"""Rectangle class inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.width *self.height
    
    def display(self):
        """Prints the Rectangle instance with the character #"""

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
    
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def  update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle instance."""

        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) >= 5:
                self.y =args[4]

        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value

                elif key == 'width':
                    self.width = value

                elif key == 'height':
                    self.height = value
                
                elif key == 'x':
                    self.x = value

                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Overrides the default __str__ method to return a string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Return dictionary represenation of a rectangle
        """

        return {
            'id' : self.id,
            'width' : self.__width,
            'height' : self.__height,
            'x' : self.__x,
            'y' : self.__y
        }