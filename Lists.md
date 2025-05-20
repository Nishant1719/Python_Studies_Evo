# Lists General Notes
- Lists are a built-in data type in Python that allow you to store and manipulate collections of items. They are mutable, meaning you can change their contents after creation. Lists can contain elements of different data types, including other lists.

- # Interview Questions: Manipulating Lists practice
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    myGames[1:3] = "AC3" # This will replace the elements at index 1 and 2 with the string "AC3"
    print(myGames) # Output: ['AC2', 'A', 'C', '3', 'GTA5']
    # The string "AC3" is treated as an array, and each character is added to the list.
    # --------------------------------------------------------
    # Why does this happen? Because strings are iterable in Python, and when you assign a string to a list slice, it unpacks the string into individual characters.
    # --------------------------------------------------------
    # To avoid this, you can use a list instead:
    myGames[1:3] = ["AC3"] # This will replace the elements at index 1 and 2 with the list ["AC3"]
    print(myGames) # Output: ['AC2', 'AC3', 'GTA5']
    ``` 
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    print(myGames[1:1]) # Output: []
    # The slice [1:1] means "start at index 1 and go up to, but not including, index 1", which results in an empty list.
    myGames[1:1] = ["AC3", "AC5"] # This will insert "AC3" at index 1
    print(myGames) # Output: ['AC2', 'AC3', 'AC5', 'GOWR', 'DMC5', 'GTA5']
    # Why does this happen? Because when you assign a list to a slice, it inserts the elements of the list at the specified index.
    ```

- # if Statement in lists
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    if "AC2" in myGames:
        print("AC2 is in the list") # Output: AC2 is in the list
    else:
        print("AC2 is not in the list")
    ```
- # Pop() method:
    - The `pop()` method removes the last element from the list and returns it. If you want to remove an element at a specific index, you can pass that index as an argument to the `pop()` method.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    print(myGames.pop()) # Output: GTA5
    print(myGames) # Output: ['AC2', 'GOWR', 'DMC5']
    # The pop() method removes the last element from the list and returns it.
    ```
- # Remove() method:
    - The `remove()` method removes the first occurrence of a specified value from the list. If the value is not found, it raises a ValueError.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    myGames.remove("GOWR") # This will remove the first occurrence of "GOWR" from the list
    print(myGames) # Output: ['AC2', 'DMC5', 'GTA5']
    ```
- # Sort() method:
    - The `sort()` method sorts the elements of the list in ascending order by default. You can also pass a custom sorting function as an argument to the `sort()` method.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    myGames.sort() # This will sort the list in ascending order
    print(myGames) # Output: ['AC2', 'DMC5', 'GOWR', 'GTA5']
    ```
- # Insert() method:
    - The `insert()` method inserts an element at a specified index in the list. The first argument is the index where you want to insert the element, and the second argument is the element you want to insert.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    myGames.insert(1, "AC3") # This will insert "AC3" at index 1
    print(myGames) # Output: ['AC2', 'AC3', 'GOWR', 'DMC5', 'GTA5']
    myGames.insert(3,"AC1") # This will insert "AC1" at index 3
    print(myGames) # Output: ['AC2', 'AC3', 'GOWR', 'AC1', 'DMC5', 'GTA5']
    ```
- # copy() : Interview Question
    - The `copy()` method creates a shallow copy of the list. This means that it creates a new list object, but the elements inside the list are still references to the original objects. If you modify the copied list, it will not affect the original list.
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
- # List Comprehension: 
    - List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering the items based on a condition.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    myGames_upper = [game.lower() for game in myGames] # This will create a new list with all elements in lowercase
    print(myGames_upper) # Output: ['ac2', 'gowr', 'dmc5', 'gta5']
    ```
    - Example:
    ```python
    squares = [x**2 for x in range(10)] # This will create a list of squares from 0 to 9
    print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
- # Range() function:
    - The `range()` function generates a sequence of numbers. It can take one, two, or three arguments: start, stop, and step. The start argument is inclusive, while the stop argument is exclusive.
    - Example:
    ```python
    myGames = ["AC2","GOWR","DMC5","GTA5"]
    for i in range(len(myGames)):
        print(myGames[i]) # This will print each element in the list
    ```
    - Example:
    ```python
    Qubes = [x**3 for x in range(10)] # This will create a list of cubes from 0 to 9
    print(Qubes) # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    ```