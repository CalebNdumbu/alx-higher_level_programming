#!/usr/bin/python3
"""defines a class that inhrits int"""

class MyInt(int):
    """inverts == and !="""

    def __eq__(self, value):
        """Override == with !="""
        return self.real != value
    
    def __ne__(self, value):
        """overide != with =="""
        return self.real == value