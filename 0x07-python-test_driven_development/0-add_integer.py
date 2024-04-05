"""
Adds up two intergers
"""

def add_integer(a, b=98):
    """Return sum of two integers
    
    Args:
        a:  first arg
        b: second arg

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If eithe =r of the arguments is not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
