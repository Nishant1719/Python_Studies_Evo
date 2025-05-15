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
