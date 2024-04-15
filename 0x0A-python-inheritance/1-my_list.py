#!/usr/bin/python3
"""module that inherits from list"""

class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))