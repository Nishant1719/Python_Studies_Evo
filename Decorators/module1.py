import time 

def timer(func):
    def wrapper(*args, **kwargs): # *args and **kwargs are used to pass any number of arguments.
                                  # *args is a tuple of positional arguments and **kwargs is a dictionary of keyword arguments.
        result = func(*args, **kwargs)
        return result
    return wrapper

    