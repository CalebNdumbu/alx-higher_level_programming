### Repository: alx-higher_level_programming

---

#### Description
This repository contains solutions to various Python tasks focusing on more advanced data structures and algorithms. Each task is designed to enhance your understanding of Python programming, particularly in the context of handling data structures efficiently.

---

#### Tasks

1. **Squared simple**
    - Write a function `square_matrix_simple(matrix)` that computes the square value of all integers of a matrix.
    - **Prototype:** `def square_matrix_simple(matrix=[]):`
    - **Constraints:**
        - `matrix` is a 2-dimensional array.
        - Returns a new matrix with the same size as the input matrix.
        - Each value in the new matrix should be the square of the corresponding value in the input matrix.
        - The input matrix should not be modified.
        - You are not allowed to import any module.

    **Example:**
    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    ```

    File: `0-square_matrix_simple.py`
    
2. **Search and replace**
    - Write a function `search_replace(my_list, search, replace)` that replaces all occurrences of an element by another in a new list.
    - **Prototype:** `def search_replace(my_list, search, replace):`
    - **Constraints:**
        - `my_list` is the initial list.
        - `search` is the element to replace in the list.
        - `replace` is the new element.
        - You are not allowed to import any module.

    **Example:**
    ```python
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    # Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    ```

    File: `1-search_replace.py`

3. **Unique addition**
    - Write a function `uniq_add(my_list=[])` that adds all unique integers in a list (only once for each integer).
    - **Prototype:** `def uniq_add(my_list=[]):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
    # Output: Result: 15
    ```

    File: `2-uniq_add.py`

4. **Present in both**
    - Write a function `common_elements(set_1, set_2)` that returns a set of common elements in two sets.
    - **Prototype:** `def common_elements(set_1, set_2):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
    # Output: ['C']
    ```

    File: `3-common_elements.py`

5. **Only differents**
    - Write a function `only_diff_elements(set_1, set_2)` that returns a set of all elements present in only one set.
    - **Prototype:** `def only_diff_elements(set_1, set_2):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
    # Output: ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
    ```

    File: `4-only_diff_elements.py`

6. **Number of keys**
    - Write a function `number_keys(a_dictionary)` that returns the number of keys in a dictionary.
    - **Prototype:** `def number_keys(a_dictionary):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
    # Output: Number of keys: 3
    ```

    File: `5-number_keys.py`

7. **Print sorted dictionary**
    - Write a function `print_sorted_dictionary(a_dictionary)` that prints a dictionary by ordered keys.
    - **Prototype:** `def print_sorted_dictionary(a_dictionary):`
    - **Constraints:**
        - You can assume that all keys are strings.
        - Keys should be sorted by alphabetic order.
        - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary).
        - Dictionary values can have any type.
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
    # Output:
    # Number: 89
    # ids: [1, 2, 3]
    # language: C
    # track: Low level
    ```

    File: `6-print_sorted_dictionary.py`

8. **Update dictionary**
    - Write a function `update_dictionary(a_dictionary, key, value)` that replaces or adds key/value in a dictionary.
    - **Prototype:** `def update_dictionary(a_dictionary, key, value):`
    - **Constraints:**
        - `key` argument will be always a string.
        - `value` argument will be any type.
        - If a key exists in the dictionary, the value will be replaced.
        - If a key doesn’t exist in the dictionary, it will be created.
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    # Output:
    # language: Python
    # number: 89
    # track: Low level
    ```

    File: `7-update_dictionary

.py`

9. **Simple delete by key**
    - Write a function `simple_delete(a_dictionary, key="")` that deletes a key in a dictionary.
    - **Prototype:** `def simple_delete(a_dictionary, key=""):`
    - **Constraints:**
        - If a key doesn’t exist, the dictionary won’t change.
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(new_dict)
    # Output:
    # language: C
    # number: 89
    ```

    File: `8-simple_delete.py`

10. **Multiply by 2**
    - Write a function `multiply_by_2(a_dictionary)` that returns a new dictionary with all values multiplied by 2.
    - **Prototype:** `def multiply_by_2(a_dictionary):`
    - **Constraints:**
        - You can assume that all values are integers.
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level", 'ids': [1, 2, 3] }
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(new_dict)
    # Output:
    # language: CC
    # number: 26
    # track: Low levelLow level
    # ids: [1, 2, 3, 1, 2, 3]
    ```

    File: `9-multiply_by_2.py`

11. **Best score**
    - Write a function `best_score(a_dictionary)` that returns a key with the biggest integer value.
    - **Prototype:** `def best_score(a_dictionary):`
    - **Constraints:**
        - If no score found, return `None`.
        - You can assume that all values are integers.
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'John': 12, 'Bob': 14, 'Chris': 13, 'Julia': 13 }
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))
    # Output: Best score: Bob
    ```

    File: `10-best_score.py`

12. **Multiply by using map**
    - Write a function `multiply_list_map(my_list=[], number=0)` that computes the square value of all integers of a matrix using map.
    - **Prototype:** `def multiply_list_map(my_list=[], number=0):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    new_list = multiply_list_map(my_list, 3)
    print(new_list)
    # Output: [3, 6, 9, 12, 15]
    ```

    File: `11-multiply_list_map.py`

13. **Roman to Integer**
    - Write a function `roman_to_int(roman_string)` that converts a Roman numeral to an integer.
    - **Prototype:** `def roman_to_int(roman_string):`
    - **Constraints:**
        - `roman_string` will be a string with at most 5 characters in uppercase.
        - `roman_string` will always be a valid Roman numeral representation.
        - You are not allowed to import any module.

    **Example:**
    ```python
    roman_string = "XIV"
    print(roman_to_int(roman_string))
    # Output: 14
    ```

    File: `12-roman_to_int.py`

14. **Weighted average!**
    - Write a function `weight_average(my_list=[])` that returns the weighted average of all integers tuple (`<score>`, `<weight>`).
    - **Prototype:** `def weight_average(my_list=[]):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Weighted average: {:.2f}".format(result))
    # Output: Weighted average: 2.80
    ```

    File: `100-weight_average.py`

15. **Squared by using map**
    - Write a function `square_matrix_map(matrix=[])` that computes the square value of all integers of a matrix using map.
    - **Prototype:** `def square_matrix_map(matrix=[]):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    ```

    File: `101-square_matrix_map.py`

16. **Delete by value**
    - Write a function `complex_delete(a_dictionary, value)` that deletes keys with a specific value in a dictionary.
    - **Prototype:** `def complex_delete(a_dictionary, value):`
    - **Constraints:**
        - You are not allowed to import any module.

    **Example:**
    ```python
    a_dictionary = { 'John': 12, 'Bob': 14, 'Chris': 13, 'Julia': 13 }
    new_dict = complex_delete(a_dictionary, 13)
    print_sorted_dictionary(new_dict)
    # Output:
    # John: 12
    # Bob: 14
    ```

    File: `102-complex_delete.py`

17. **CPython #1: PyBytesObject**
    - C functions that print basic info about Python lists and Python bytes objects.
    - **Note:** This task involves writing C code.

    File: `103-python.c`
