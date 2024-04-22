#!/usr/bin/python3
"""base for other classes"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ base constructor"""
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects