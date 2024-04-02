#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints all elements of a list
    """

    count = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
        except IndexError:
            break
        else:
            count += 1
    print()
    return count
