# Dictionaries : Important Data Structure in Python and web development.
- # Dictionaries are mutable, unordered collections of key-value pairs.
    - They are defined using curly braces `{}` and can contain elements of different data types, including other dictionaries.
    -  Each key in a dictionary must be unique, and it is used to access the corresponding value.
    -  Values in a dictionary can be of any data type, including lists, tuples, and other dictionaries.
    -  Dictionaries are useful for storing and manipulating data that is associated with specific keys, such as configuration settings, user profiles, and more.
- # Example:
```python
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"]) # Output: John
print(my_dict["age"]) # Output: 30
print(my_dict["city"]) # Output: New York
```
- # Adding a new key-value pair:
```python
my_dict["country"] = "USA"
print(my_dict["country"]) # Output: USA
```
- # Updating an existing key-value pair:
```python
my_dict["age"] = 31
print(my_dict["age"]) # Output: 31
```
- # Removing a key-value pair:
```python
del my_dict["city"]
print(my_dict) # Output: {'name': 'John', 'age': 31, 'country': 'USA'}
``` 
- # Checking if a key exists in the dictionary:
```python
if "name" in my_dict:
    print("Name exists in the dictionary")
else:
    print("Name does not exist in the dictionary")
```
- # Iterating through the keys and values of a dictionary:
```python
for key, value in my_dict.items():
    print(f"{key}: {value}") # Output: name: John, age: 31, country: USA
    # f is a formatted string literal, also known as an f-string, which allows you to embed expressions inside string literals using curly braces {}
```
- # Pop a key-value pair from the dictionary:
```python
value = my_dict.pop("age") # Key should be mentioned.
print(value) # Output: 31
print(my_dict) # Output: {'name': 'John', 'country': 'USA'}
```

- # Popitem() method: 
```python
key, value = my_dict.popitem() # Removes the last inserted key-value pair
# Note: The order of items in a dictionary is not guaranteed to be the same as the order in which they were added. So, the last inserted item may not be the last one in the dictionary.
print(key)   # Output: country
print(value) # Output: USA
print(my_dict) # Output: {'name': 'John', 'age': 31}
```
- # Copying a dictionary:
```python
my_dict_copy = my_dict.copy()
print(my_dict_copy) # Output: {'name': 'John', 'age': 31, 'country': 'USA'}
```
# Nested dictionaries: Practice
```python
my_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "state": "NY"
    }
}
print(my_dict["address"]["city"]) # Output: New York
```
- # Iterating through a nested dictionary:
```python
for key, value in my_dict.items():
    if isinstance(value, dict): # why we use this? Why to check if value is a dictionary? Answer : Because the value is another dictionary, we need to iterate through its key-value pairs.
        for sub_key, sub_value in value.items():
            print(f"{key} -> {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")
```
- isinstance() function: 
    - The `isinstance()` function is used to check if an object is an instance of a specified class or data type.
    - It returns `True` if the object is an instance of the specified class or data type, and `False` otherwise.
    - Syntax: `isinstance(object, classinfo)`
    - Example:
```python
print(isinstance(my_dict, dict)) # Output: True
print(isinstance(my_dict["name"], str)) # Output: True
print(isinstance(my_dict["age"], int)) # Output: True
print(isinstance(my_dict["address"], dict)) # Output: True
print(isinstance(my_dict["address"]["city"], str)) # Output: True
```
- # Clearing a dictionary:
```python
my_dict.clear()
print(my_dict) # Output: {}
```
- # Dictionary comprehension:
    - Dictionary comprehension is a concise way to create dictionaries in Python.
    - It allows you to create a new dictionary by applying an expression to each item in an iterable (like a list or another dictionary).
    - Syntax: `{key_expression: value_expression for item in iterable}`
```python
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
- # Fromkeys() method:
    - The `fromkeys()` method creates a new dictionary with the specified keys and a default value.
    - Syntax: `dict.fromkeys(keys, value)`
    - Example:
```python
keys = ["name", "age", "city"]
default_value = None
my_dict = dict.fromkeys(keys, default_value)
print(my_dict) # Output: {'name': None, 'age': None, 'city': None}
```

