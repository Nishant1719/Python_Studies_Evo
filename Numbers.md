 # General Notes

 - # Operator precedence Table
   - https://docs.python.org/3/reference/expressions.html#operator-precedence

- # Operators
  - '%' Modulo operator:
    - Returns the remainder of the division of two numbers.
    - Example:
    ```python
    a = 10
    b = 3
    c = a % b
    print(c) # 1
    ```
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
- # repr() vs str() vs print()
  - repr() is used to get the string representation of an object that can be used to recreate the object.
  - str() is used to get the string representation of an object that is more user-friendly.
  - print() is used to print the string representation of an object to the console.
  - Example:
  ```python
  a = 5
  b = "Hello"
  print(repr(a)) # '5'
  print(str(a)) # '5'
  print(repr(b)) # 'Hello'
  print(str(b)) # 'Hello'
  print(b) # Hello
  ```
- Boolean Operators:
  - and: Returns True if both operands are True.
  - or: Returns True if at least one operand is True.
  - not: Returns True if the operand is False, and vice versa.
  reprs are used in boolean operators to get the string representation of the boolean value.Although in python,boolean are treated as numbers category.
  - Example:
  ```python
  a = True
  b = False
  c = a and b
  d = a or b
  e = not a
  print(c) # False
  print(d) # True
  print(e) # False
  ```


    
