# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

# solution :
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Arguments values: ",args_value)
        print(f"Key-Value arguements: ",kwargs_value)
        print(f"Function Name : {func.__name__} & its arguments {args,kwargs}")
        return func(*args, **kwargs)
    return wrapper 

@debug
def greet(name,message,greeting="Hello"):
    return print(f"{name}, {greeting} Message : {message}")
    
greet("Nishant",greeting="Namaste",message="Hi there people")
# ------------------------------------------------------------------------------------
# Examples with no arguements:
# def debug_no_parameters(func):
#     def wrapper():
#         print("Decorator is called!")
#         return func()
#     return wrapper 

# @debug_no_parameters
# def print_my_name():
#     return print("Nishant")

# print_my_name()

# ------------------------------------------------------------------------------------
# Example:
# def show(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args,**kwargs)
#         print(f"function Name : {func.__name__} Arguments {args} result : {result}")
#         return result
#     return wrapper

# @show
# def cal(a,b):
#     return a+b

# Example usage:
# show(cal)(10, 20)  # This will call the cal function with arguments 10 and 20 and print the function name, arguments, and result.
# result = cal(2, 3)  # This will print the function name, arguments, and result.
# print(result)


