# Problem: Compute the factorial of a number using a (while loop).
# my sol: from for loop
num = int(input("Enter the number: "))

# While loop
result = 1
while num > 0:
    result = result * num
    num-=1
    
print(result)