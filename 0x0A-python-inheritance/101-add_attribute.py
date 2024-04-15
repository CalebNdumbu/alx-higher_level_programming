#!/usr/bin/python3

"""define a function that adds attributes of objects"""

def add_attribute(object, attr_name, value):
    """add a new attribute to an object if it's possible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)