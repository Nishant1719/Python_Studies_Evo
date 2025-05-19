# Personal Notes
- 2 ** 3 = 8 : Double star operator is used for exponentiation or power of the number.
- deepcopy() : Also Copy the nested objects.
- is operator : Used to check the identity of the object.
    - Example:
    ```python
    a = [1, 2, 3]
    b = a
    b is a # True
    a is b # True
    b = [1, 2, 3] # Explicitly creating a new object in the memory
    b is a # False
    a is b # False
    ```
    
- == operator : Used to check the equality of the object.
    Example:
    ```python
    a = [1, 2, 3]
    b = a
    b == a # True
    a == b # True

    b = [1, 2, 3] # Explicitly creating a new object in the memory
    b == a # True
    a == b # True
    ```
    
- type() : Used to check the type of the object.
    Example:
    ```python
    a = [1, 2, 3]
    print(type(a)) # <class 'list'>
    ```