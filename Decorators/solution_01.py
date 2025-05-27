import time 

def timer(func):
    def wrapper(*args, **kwargs): # why parameters are passed in wrapper?
        # Because we want to pass any number of arguments to the original function.
        # but didnt func already have parameters?
        # Yes, but when we use the @timer decorator, we want to be able to pass any arguments to the original function.
        # meaning, we want to be able to call the original function with any number of arguments.
        # So, we use *args and **kwargs to pass any number of positional and keyword arguments to the original function.
        start_time = time.time()              
        result = func(*args, **kwargs) # we are not even passing any dict ir list here, so why **kwargs its not giving error?
        # Because **kwargs is used to pass keyword arguments to the original function, and it can be empty. 
        # So, even if we don't pass any keyword arguments, it will still work.
        # If we had used only **kwargs, it would have given an error if we tried to pass positional arguments.
        end_time = time.time()
        print(f"{func.__name__} Start time : {start_time} ; End time : {end_time} Result : {result}")
        return result
    return wrapper

@timer
def cal(a,b):
    return a+b

# print(cal(2,3))
# Example usage:
timer(cal)(10, 20)  # This will call the cal function with arguments 10 and 20 and print the time taken.

# time_taken = timer(cal)
# time_taken(10, 20)
