#!/usr/bin/python3

"""Contain square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    "Represents a square"

    def __init__(self, size, x=0, y=0, id=None):
       super().__init__(size, size, x, y, id)
    
    
    @property
    def size(self):
        """Get the value of size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter method for size"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.size = args[1]

            if len(args) >= 3:
                self.x = args[2]

            if len(args) >= 4:
                self.y =args[3]

        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value

                elif key == 'size':
                    self.size = value
                
                elif key == 'x':
                    self.x = value

                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return dictionary represenation of a rectangle
        """

        return {
            'id' : self.id,
            'size' : self.size,
            'x' : self.x,
            'y' : self.y
        }