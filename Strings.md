# General Notes

- # Slice Hopping
  - Slice hopping is a technique used to extract specific elements from a sequence (like a string, list, or tuple) by specifying a start index, an end index, and a step value.
  - The syntax for slice hopping is `sequence[start:end:step]`, where:
    - `start` is the index where the slice begins (inclusive).
    - `end` is the index where the slice ends (exclusive).
    - `step` is the interval between each index in the slice.
    - Example:
    ```python
    my_string = "Hello, World!"
    print(my_string[::2])   # Output: Hlo ol!
    ```
    Example with negative step:
    ```python
    my_string = "Hello, World!"
    print(my_string[::-1])  # Output: !dlroW ,olleH
    ```
    Explanation:
    - The first example `my_string[::2]` extracts every second character from the string, starting from index 0.
    - The second example `my_string[::-1]` reverses the string by using a negative step.
    
- # strip : Web-development Practices
  - The `strip()` method is used to remove leading and trailing whitespace characters from a string.
  - Example:
  ```python
  my_string = "   Hello, World!   "
  print(my_string.strip())  # Output: "Hello, World!"
  ```
- # split : Web-development Practices
  - The `split()` method is used to divide a string into a list of substrings based on a specified delimiter.
  - Example:
  ```python
  my_string = "Hello, World!"
  print(my_string.split(", "))  # Output: ['Hello', 'World!']
  ```
- # count : Web-development Practices
  - The `count()` method is used to count the occurrences of a specified substring in a string.
  - Example:
  ```python
  my_string = "Hello, World!"
  print(my_string.count("o"))  # Output: 2
  ```
- # format : Web-development Practices
  - The `format()` method is used to format strings by inserting values into placeholders defined by curly braces `{}`.
  - Example:
  ```python
  name = "Alice"
  age = 30
  formatted_string = "My name is {} and I am {} years old.".format(name, age)
  print(formatted_string)  # Output: My name is Alice and I am 30 years old.
  ```
- # join : Web-development Practices
  - The `join()` method is used to concatenate a list of strings into a single string, with a specified separator.
  - Example:
  ```python
  my_list = ["Hello", "World"]
  joined_string = ", ".join(my_list)
  print(joined_string)  # Output: Hello, World
  ```
- # len() : Web-development Practices
  - The `len()` function is used to determine the length of a string (or other iterable).
  - Example:
  ```python
  my_string = "Hello, World!"
  print(len(my_string))  # Output: 13
  ```

- # """ and ''' : Web-development Practices
  - Triple quotes are used in Python to create multi-line strings or docstrings.
  - Example:
  ```python
  multi_line_string = """This is a string
  that spans multiple lines."""
  print(multi_line_string)
  ```
  - Example of a docstring:
  ```python
  def my_function():
      \"\"\"This is a docstring.
      It provides information about the function.
      \"\"\"
      pass
  ```   
  - Help Url : https://www.youtube.com/watch?v=ekrgx893sig&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=9
    - Timestamp : 24:05 / 30:43

- # Raw Strings
  - Raw strings are created by prefixing a string literal with an 'r' or 'R'. They treat backslashes as literal characters and do not interpret them as escape characters.
  - Example:
  ```python
  raw_string = r"This is a raw string with a backslash: \n"
  print(raw_string) # Output: This is a raw string with a backslash: \n
  ```
  Problem:
  ```python
    my_string = "Hello World\"
    print(my_string)  # Output: SyntaxError: EOL while scanning string literal

    # solution: remove the backslash at the end of the string or add one more backslash.
    my_string = "Hello World\\"
    or
    my_string = r"Hello World\" # SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
    print(my_string)  # Output: Hello World\
    ```
    - Help Url : https://www.youtube.com/watch?v=ekrgx893sig&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=9
    - Timestamp : 28:05 / 30:43

- # in : Web-development Practices
  - The `in` operator is used to check if a substring exists within a string.
  - Example:
  ```python
  my_string = "Hello, World!"
  print("World" in my_string)  # Output: True
  ```