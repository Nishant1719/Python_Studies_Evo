# Problem: Create a recursive function to calculate the factorial of a number.

def my_factorial(number):
    if number==0: return 1
    else: return number * my_factorial(number-1)

print(my_factorial(5))

# Always find how to exit the function 
# Exit strategies are important in the recursive function