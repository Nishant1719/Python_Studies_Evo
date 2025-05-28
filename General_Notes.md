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
- # not operator : Used to negate the condition.
    - Example:
    ```python
    if not (a == 1):
        print("a is not equal to 1")
    ```
- # Named arguements : Used to pass the arguments to the function by name.
    - Example:
    ```python
    def add(name1, name2):
        return name1 + name2
    print(add(name2=2, name1=1)) # 3
    ```
    - Even when the order of the arguments is changed, it will still work.
    
# Very Important for DSA :
- # URL:
    - https://www.youtube.com/watch?v=_VxQ5jzo37o&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=15

# Django Important Notes:
- # Decorators:
    - # Factory functions or closure functions:
        - Used to create a function that returns another function.
        - Example:
        ```python
        def outer_function(x):
            def inner_function(y):
                return x + y
            return inner_function
        add_five = outer_function(5)
        print(add_five(10)) # 15
        ```
- # ennumerate() :
    - Used to iterate over a list and get the index and value of the element.
    - Example:
    ```python
    my_list = ["a", "b", "c"]
    for index, value in enumerate(my_list):
        print(index, value)
    # Output:
    # 0 a
    # 1 b
    # 2 c
    ```
    Example:
    ```python
    my_list = [{"name": "nishant", "time": "55 mins"}, {"name": "shreya", "time": "35 mins"}, {"name": "trainer", "time": "1 hours"}]
    # emu_list = enumerate(my_list)
    # for index, value in emu_list:
        # print(index, value) # Output:
        # 0 {'name': 'nishant', 'time': '55 mins'}
        # 1 {'name': 'shreya', 'time': '35 mins'}
        # 2 {'name': 'trainer', 'time': '1 hours'}
    for index, value in enumerate(my_list, start=1):
        print(f"{index}. {value['name']} - {value['time']}")
    # Output:
    # 1. nishant - 55 mins
    # 2. shreya - 35 mins
    # 3. trainer - 1 hours
    ```
- # zip() : 
    - Used to combine two or more lists into a single list of tuples.
    - Example:
    ```python
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    zipped = zip(list1, list2)
    print(list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]
    ```
- # map() :
    - Used to apply a function to all the items in an iterable (like a list).
    - Example:
    ```python
    def square(x):
        return x * x
    numbers = [1, 2, 3, 4]
    squared_numbers = map(square, numbers)
    print(list(squared_numbers)) # [1, 4, 9, 16]
    ```

