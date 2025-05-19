 # General Notes

 - # Operator precedence Table
   - https://docs.python.org/3/reference/expressions.html#operator-precedence

- # Good practices :
    - Always use same type of data or value when using operators.
    Example: 
    ```python
    a = 5
    b = 10
    c = a + b
    ```
    Example of bad practice:
    ```python
    a = 5
    b = 10.0
    c = a + b
    ```
    - Type Casting: Solution for the above bad practice.
    ```python
    a = 5
    b = 10.0
    c = a + int(b)
    print(c) # 15
    ```

    
