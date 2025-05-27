# Problem: Create a lambda function to compute the cube of a number.
# Lambda Functions are basically nameless functions 
# Uses : if the function is not gonna be used soo many times :
# Url  : https://www.youtube.com/watch?v=JptOj-D6gtw&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=16
# timestamp : 23:00


cube = lambda x: x ** 3 
# print(cube) # Stores memory address.
print(cube(3)) # Prints values.

# Why lambda?
# Ans : Because it is a nameless function and we can use it in places where we don't need to reuse the function.
# also it is a one-liner function.
