# Personal Notes
- 2 ** 3 = 8 : Double star operator is used for exponentiation or power of the number.

- # Random number 
    Random number generation in Python can be done using the `random` module.
    - `random.randint(a, b)` generates a random integer between `a` and `b`, inclusive.
        Example: 
            >>> import random as r
            >>> r.randint(1, 10)
            7
    - `random.random()` generates a random float between 0.0 and 1.0.
        Example: 
            >>> import random as r
            >>> r.random()
            0.24034527403896244
        
    - `random.choice(sequence)` randomly selects an element from a non-empty sequence.
        Example:
            >>> import random as r
            >>> r.choice([1, 2, 3, 4, 5])
            3

    - `random.shuffle(sequence)` shuffles the elements of a list in place.
        Example:
            >>> import random as r
            >>> lst = [1, 2, 3, 4, 5]
            >>> r.shuffle(lst)
            >>> lst
            [3, 1, 4, 5, 2]

- # Strings 
    - Strings are immutable in Python, meaning they cannot be changed after creation.
    - Can be used as a list/array of characters internally.
    Example:
        >>> s = "hello"
        >>> s[0]
        'h'
        >>> s[1:4]
        'ell'
        >>> s[-1]
        'o'

- To Explore methods in any data type, use the `dir()` function.
    Example:
        >>> dir(str)
        ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format']
    
    Example:
        >>> dir(list)
        ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 'append', 'clear']

    Example:
        >>> dir(123)
        ['__abs__', '__add__', '__and__', '__annotations__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__float__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__']