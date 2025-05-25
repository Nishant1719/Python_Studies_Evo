# Problem: Calculate the sum of even numbers up to a given number n.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10] # 2
total = 0
for n in numbers:
    if n%2 == 0:
        total = total + n
        
print("Result :",total)