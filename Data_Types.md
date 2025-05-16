# DATA TYPES (Obj Types)

- # Mutable
    - List : [1,2,3], [1,2,3.0], [1,2,'a'], [1,2,[3,4]], list(range(10))
        - Mutable
        - Ordered
        - Can contain duplicates
        - Can contain mixed data types
        - Can contain nested lists
        - Can contain empty lists

    

    - Set : {1,2,3}, {1,2,3.0}, {1,2,'a'}, {1,2,(3,4)}, set(range(10))
        -Values must be unique
        - Unordered
        

    - Dict : {'a':1, 'b':2}, {1:'a', 2:'b'}, {1:1.0, 2:2.0}, {1:1.0, 2:'a'}, dict(a=1, b=2)
        - Key-Value pairs
        - Unordered
        - Keys must be unique

- # Immutable
    - Number : 1234,3.123,3+4j,0b111,Decimal(),Fraction()

    - String : 'spam', "Nishant", b'a\x01c' (Special), u'sp\xc4m' <Unicode> (Special)

    - Tuple : (1,2,3), (1,2,3.0), (1,2,'a'), (1,2,(3,4)), tuple('MyTuple', range(10))
        - Immutable
        - Ordered
        - Can contain duplicates
        - Can contain mixed data types
        - Can contain nested tuples
        - Can contain empty tuples

    - None : None 
        - Represents absence of value

    - Boolean : True, False

- # Advanced
    - Decorators
    - Generators
    - Iterators

- # Meta-Programming

- # Random number 
    Random number generation in Python can be done using the `random` module.
    - `random.randint(a, b)` generates a random integer between `a` and `b`, inclusive.
        Example: 
        ```python
        import random as r
        r.randint(1, 10) # 7 output may vary
        ```

    - `random.random()` generates a random float between 0.0 and 1.0.
        Example: 
        ```python
        import random as r
        r.random() # output may vary 0.24034527403896244
        ```
    - `random.choice(sequence)` randomly selects an element from a non-empty sequence.
        Example:
        ```python
        import random as r
        r.choice([1, 2, 3, 4, 5])
        3 # output may vary 
        ```

    - `random.shuffle(sequence)` shuffles the elements of a list in place.
        Example:
        ```python
        import random as r
        lst = [1, 2, 3, 4, 5]
        r.shuffle(lst) # output may vary
        lst # output may vary [2, 4, 1, 5, 3]
        ```
- # Strings 
    - Strings are immutable in Python, meaning they cannot be changed after creation.
    - Can be used as a list/array of characters internally.
        Example:
        ```python
        s = "hello"
        s[0] # output is 'h'
        s[1:4] # output is 'ell'
        s[-1] # output is 'o'
        ```
- # To Explore methods in any data type, use the `dir()` function.
    Example:
        >>> dir(str)
        ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format']
    
    Example:
        >>> dir(list)
        ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 'append', 'clear']

    Example:
        >>> dir(123)
        ['__abs__', '__add__', '__and__', '__annotations__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__float__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__']

- # Dictionaries
    - Dictionaries are mutable and unordered collections of key-value pairs.
    - Keys must be unique and immutable (e.g., strings, numbers, tuples).
    - Values can be of any data type and can be duplicated.
    - Example:
        ```python
        my_dict = {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        }
        ```
    - Accessing values:
        ```python
        print(my_dict["name"])  # Output: Alice
        ```
    - Adding a new key-value pair:
        ```python
        my_dict["job"] = "Engineer"
        ```
    - Removing a key-value pair:
        ```python
        del my_dict["age"]
        ```
    - Iterating through keys:
        ```python
        for key in my_dict:
            print(key)
        ```
    - Iterating through values:
        ```python
        for value in my_dict.values():
            print(value)
        ```
    - Iterating through key-value pairs:
        ```python
        for key, value in my_dict.items():
            print(key, value)
        ```
- # Tuples
    - Tuples are immutable sequences, meaning they cannot be changed after creation.
    - They can contain elements of different data types.
    - Example:
        ```python
        my_tuple = (1, "hello", 3.14)
        ```
    - Accessing elements:
        ```python
        print(my_tuple[0])  # Output: 1
        ```
    - Slicing:
        ```python
        print(my_tuple[1:3])  # Output: ('hello', 3.14)
        ```
    - Tuples can be used as keys in dictionaries because they are immutable.
        ```python
        MyTup =  (1, 2)
        print(MyTup[0]) # Output: 1
        ```