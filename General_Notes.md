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

- print("Hello", end="-") : Used to print the string without a new line.
    Example:
    ```python
    print("Hello", end="-") # Hello-
    ```
    Example:
    ```python
    Games = ["AC2", "GOWR", "DMC5", "GTA5"]
    for i in range(len(Games)):
        print(Games[i], end="-") # AC2-GOWR-DMC5-GTA5-
    ```

- Copy() : Used to create a shallow copy of the list.
    Example:
    ```python
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 4
    print(a) # [1, 2, 3]
    print(b) # [4, 2, 3]
    ```
    - Problem:
    ```python
    Games = ["AC2", "GOWR", "DMC5", "GTA5"]
    Games_copy = Games # Copying the list but not creating a new object in the memory.
    # It has the same reference as the original list.
    # so if we change the copied list, it will also change the original list.
    Games_copy[0] = "AC3"
    print(Games) # ['AC3', 'GOWR', 'DMC5', 'GTA5']
    print(Games_copy) # ['AC3', 'GOWR', 'DMC5', 'GTA5']
    ```
    - Solution:
    ```python
    Games = ["AC2", "GOWR", "DMC5", "GTA5"]
    Games_copy = Games.copy() # Copying the list and creating a new object in the memory.
    # Now if we change the copied list, it will not change the original list.
    Games_copy[0] = "AC3"
    print(Games) # ['AC2', 'GOWR', 'DMC5', 'GTA5']
    print(Games_copy) # ['AC3', 'GOWR', 'DMC5', 'GTA5']
    ```
    