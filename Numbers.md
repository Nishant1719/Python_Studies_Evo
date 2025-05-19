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
- # Boolean Operators:
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

- # Libraries :
  - math: Provides mathematical functions and constants.
    - math.floor(x): Returns the largest integer less than or equal to x.
    Example:
    ```python
    import math
    a = 5.7
    b = math.floor(a)
    print(b) # 5
    ```
    - math.trunc(x): Returns the integer part of x. Towards zero.
    Example:
    ```python
    import math
    a = 5.7
    b = math.trunc(a)
    print(b) # 5
    ```
- # octal, hex, bin:
  - oct(x): Converts x to octal string.
    - octal is a base-8 number system that uses digits 0-7.
  - hex(x): Converts x to hexadecimal string.
    - hexadecimal is a base-16 number system that uses digits 0-9 and letters A-F.
  - bin(x): Converts x to binary string.
    - binary is a base-2 number system that uses digits 0 and 1.
  - Example:
  ```python
  a = 10
  b = oct(a)
  c = hex(a)
  d = bin(a)
  print(b) # '0o12'
  print(c) # '0xa'
  print(d) # '0b1010'
  ```
  - # int(x, base): (Alternative to oct, hex, bin methods)
    - Converts x to an integer in the given base.
    - Example:
    ```python
    a = '0o12'
    b = int(a, 8)
    print(b) # 10
    a = '0xa'
    b = int(a, 16)
    print(b) # 10
    a = '0b1010'
    b = int(a, 2)
    print(b) # 10
    ```

- # Bitwise Operators:
  - & (AND): Returns 1 if both bits are 1, otherwise returns 0.
  - | (OR): Returns 1 if at least one bit is 1, otherwise returns 0.
  - ^ (XOR): Returns 1 if the bits are different, otherwise returns 0.
  - ~ (NOT): Inverts the bits.
  - << (Left Shift): Shifts the bits to the left by the given number of positions.
  - >> (Right Shift): Shifts the bits to the right by the given number of positions.
  - Example:
  ```python
  a = 10 # 1010 in binary
  b = 4  # 0100 in binary
  c = a & b # check if both bits are 1.
  d = a | b # check if at least one bit is 1.
  e = a ^ b # check if the bits are different.
  f = ~a # invert the bits.
  g = a << 1 # basically operation happens like a * 2 ^ n , Where n is the number of positions
  h = a >> 1 # basically operation happens like a // 2 ^ n , Where n is the number of positions
  print(c) # 0
  print(d) # 14
  print(e) # 14
  print(f) # -11
  print(g) # 20
  print(h) # 5
  ```
  - # Bitwise Table :
  | Operator | Description |
  |----------|-------------|
  | &        | AND         |
  | \|      | OR          |
  | ^        | XOR        |
  | ~        | NOT        |
  | <<       | Left Shift  |
  | >>       | Right Shift |

  - # Bitwise short-hand table:
  1. AND (&) — Bitwise AND
    Bit A	  Bit B	  A & B (AND)
    0	      0	      0
    0	      1	      0
    1	      0	      0
    1	      1	      1
  2. OR (|) — Bitwise OR
    Bit A	  Bit B	  A | B (OR)
    0	      0	      0
    0	      1	      1
    1	      0	      1
    1	      1	      1
  3. XOR (^) — Bitwise XOR
    Bit A	  Bit B	  A ^ B (XOR)
    0	      0	      0
    0	      1	      1
    1	      0	      1
    1	      1	      0
  4. NOT (~) — Bitwise NOT
    Bit A	  ~A (NOT)
    0	      1
    1	      0
  
- # Random: (Easy implementation)
  - random.randint(a, b): Returns a random integer between a and b (inclusive).
  Example:
  ```python
  import random
  a = random.randint(1, 10)
  print(a) # Random integer between 1 and 10
  ```
  - random.choice(seq): Returns a random element from the non-empty sequence seq.
  Example:
  ```python
  import random
  a = random.choice([1, 2, 3, 4, 5])
  print(a) # Random element from the list
  ```