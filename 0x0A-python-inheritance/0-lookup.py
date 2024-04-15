#!/usr/bin/python3
"""
 returns the list of available attributes and methods of an object
"""

def lookup(obj):
    """looks for all attributes"""
    return dir(obj)