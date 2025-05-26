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

- Always Use paranthesis is multiple conditional statements.
    - # why?
    - Because it makes the code more readable and avoids confusion.
    Example:
    ```python
    if (a == 1 and b == 2) or (c == 3 and d == 4):
        print("True")
    ```

# Very Important for DSA :
- # URL:
    - https://www.youtube.com/watch?v=_VxQ5jzo37o&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=15