# !/usr/bin/python3

"""

Contains a function that indents texts

"""

def text_indentation(text):
    """ Prints a text with two new lines after each '.' , '?' or ':'

    Args:
        text : The string to be printed

    Raises:
        TypeError: If text is not a string
    
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    count = 0

    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1