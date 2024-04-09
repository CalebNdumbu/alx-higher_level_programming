#!/usr/bin/python3

"""
Contains a function that prints a square

"""

def print_square(size):
    """Prints a square with # character
    
    Args:
        size: integer that represents length of the square to print

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is a float and less than zero
        TypeError: If size is a float and less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    elif size < 0:
        raise ValueError("size must br >= 0")
    
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")

    