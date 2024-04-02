def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists.

    Args:
        my_list_1: First list.
        my_list_2: Second list.
        list_length: Length of the resulting list.

    Returns:
        A new list with all the divisions.
    """
    new_list = []

    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    
    return (new_list)