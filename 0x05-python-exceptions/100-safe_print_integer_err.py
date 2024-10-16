#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Function that prints an integer
    """
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    else:
        return True
