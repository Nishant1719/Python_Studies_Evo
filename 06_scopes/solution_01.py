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
        return x ** num # num : will be treated as global variable here
    return sub_func

result = main_func(2)
print(result(3)) # Output : It will be sqrt of 3 as per the func defination.

