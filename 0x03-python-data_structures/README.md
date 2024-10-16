# Python Data Structures

This repository contains solutions to various tasks related to Python data structures from the ALX Higher Level Programming curriculum.

## Task List:

1. **Print a list of integers**
   - Write a function that prints all integers of a list.
   - Prototype: `def print_list_integer(my_list=[]):`
   - Format: one integer per line. See example.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use str.format() to print integers.

2. **Secure access to an element in a list**
   - Write a function that retrieves an element from a list like in C.
   - Prototype: `def element_at(my_list, idx):`
   - If idx is negative, the function should return None.
   - If idx is out of range (> of number of element in my_list), the function should return None.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

3. **Replace element**
   - Write a function that replaces an element of a list at a specific position (like in C).
   - Prototype: `def replace_in_list(my_list, idx, element):`
   - If idx is negative, the function should not modify anything, and returns the original list.
   - If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

4. **Print a list of integers... in reverse!**
   - Write a function that prints all integers of a list, in reverse order.
   - Prototype: `def print_reversed_list_integer(my_list=[]):`
   - Format: one integer per line. See example.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use str.format() to print integers.

5. **Replace in a copy**
   - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
   - Prototype: `def new_in_list(my_list, idx, element):`
   - If idx is negative, the function should return a copy of the original list.
   - If idx is out of range (> of number of element in my_list), the function should return a copy of the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

6. **Can you C me now?**
   - Write a function that removes all characters 'c' and 'C' from a string.
   - Prototype: `def no_c(my_string):`
   - The function should return the new string.
   - You are not allowed to import any module.
   - You are not allowed to use str.replace().

7. **Lists of lists = Matrix**
   - Write a function that prints a matrix of integers.
   - Prototype: `def print_matrix_integer(matrix=[[]]):`
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use str.format() to print integers.

8. **Tuples addition**
   - Write a function that adds 2 tuples.
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
   - Returns a tuple with 2 integers.
   - You are not allowed to import any module.
   - You can assume that the two tuples will only contain integers.
   - If a tuple is smaller than 2, use the value 0 for each missing integer.
   - If a tuple is bigger than 2, use only the first 2 integers.

9. **More returns!**
   - Write a function that returns a tuple with the length of a string and its first character.
   - Prototype: `def multiple_returns(sentence):`
   - If the sentence is empty, the first character should be equal to None.
   - You are not allowed to import any module.

10. **Find the max**
    - Write a function that finds the biggest integer of a list.
    - Prototype: `def max_integer(my_list=[]):`
    - If the list is empty, return None.
    - You can assume that the list only contains integers.
    - You are not allowed to import any module.
    - You are not allowed to use the builtin max().

11. **Only by 2**
    - Write a function that finds all multiples of 2 in a list.
    - Prototype: `def divisible_by_2(my_list=[]):`
    - Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2.
    - The new list should have the same size as the original list.
    - You are not allowed to import any module.

12. **Delete at**
    - Write a function that deletes the item at a specific position in a list.
    - Prototype: `def delete_at(my_list=[], idx=0):`
    - If idx is negative or out of range, nothing changes (returns the same list).
    - You are not allowed to use pop().
    - You are not allowed to import any module.

13. **Switch**
    - Complete the source code to switch the values of a and b.
    - You can find the source code in the repository.

14. **Linked list palindrome**
    - Write a function in C that checks if a singly linked list is a palindrome.
    - Prototype: `int is_palindrome(listint_t **head);`
    - Return: 0 if it is not a palindrome, 1 if it is a palindrome.
    - An empty list is considered a palindrome.
    
15. **CPython #0: Python lists**
    - Create a C function that prints some basic info about Python lists.

