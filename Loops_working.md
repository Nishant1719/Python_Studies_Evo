# Behind the Scenes of Loops

- # Iteration Tools in python:
    - `for` loops
    - `while` loops
    - `break` and `continue`
    - `range()`
    - List comprehensions
    - map, filter, and reduce functions
    
    |
    |   iter()
    V

- # Iterable objects:
    - Strings
    - Lists
    - Tuples
    - Dictionaries
    - Sets
    - files

    |
    |
    V

- # Response (__next__):
    - `next()` function
    - `iter()` function
    - `StopIteration` exception

- # iter() :
    - Converts an iterable object into an iterator.
    - Example:
    ```python
    my_list = [1, 2, 3]
    my_iter = iter(my_list) # Output: <list_iterator object at 0x...> , gives memory starting address
    print(next(my_iter))  # Output: 1
    print(next(my_iter))  # Output: 2
    print(next(my_iter))  # Output: 3
    ```
    
- # What is an Iterator and iterable?
    - An **iterator** is an object that implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`.
    - An **iterable** is any object that can return its members one at a time, and it must implement the `__iter__()` method.

- # URL : https://www.youtube.com/watch?v=_VxQ5jzo37o&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=15