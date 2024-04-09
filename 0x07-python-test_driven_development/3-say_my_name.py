#!/usr/bin/python3

"""
 Has a function that prints a name   
"""

def say_my_name(first_name, last_name=""):
    """Function prints  <first name> <last name>

    Args:
        first_name : the first name to print
        last_name : the last name to print

    Raises:
        TypeError : if either first_name or last_name isn't a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)