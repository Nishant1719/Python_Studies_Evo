 # Something new :
 
x = 99
 
# def func():
#     global x # this give x a global reference (considered Bad Practice) (Not reliable).
#     x = 17
    
# func()
# print(x)  

# Example
# def f1():
#     # x = 29 # if x is not available here it will goes to global scope of f1() which is a real global scope.
#     def f2():
#         print(x) # Output : 29 , as its global space func f1
#     f2()
    
# f1()


# Example
def f1():
    x = 29 # if x is not available here it will goes to global scope of f1() which is a real global scope.
    def f2():
        print(x) # Output : 29 , as its global space func f1
    return f2
    
myresult = f1()
myresult() # it will execute the f2 func.

# Factory functions / closure functions 
def main_func(num):
    def sub_func(x):
        return x ** num # num : will be treated as global variable here / returns the x raised to the power of num.
    return sub_func # This returns a function after executing the sub_func function.
# This is a closure function, as it remembers the value of num even after main_func has finished executing.
# why? Because sub_func is defined inside main_func and has access to its variables.
# so ? it can use the value of num even after main_func has completed.
# as sub_func is returned from main_func, it retains access to num. plus its not called yet.

result = main_func(2)
result_2 = main_func(3)
print(result(3)) # Output : 9, as per the func definition (3 ** 2).
print(result_2(3)) # Output : 27, as per the func definition (3 ** 3).

# Incase of result : result holds a reference to the sub_func function, which has access to the num variable which is 2. in this case.
# Incase of result_2 : result_2 holds a reference to the sub_func function, which has access to the num variable which is 3. in this case.
# So, when we call result(3), it returns 3 raised to the power of 2, and when we call result_2(3), it returns 3 raised to the power of 3.
# This is a powerful feature of Python, allowing you to create functions that can remember values from their enclosing scope.