#!/usr/bin/python3

"""Chaeck if object is an instance of, or is an instance of a ckass inherited"""

def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, 
    or if the object is an instance of a class that 
    inherited from, the specified class ; otherwise False
    """
    return (isinstance(obj, a_class))