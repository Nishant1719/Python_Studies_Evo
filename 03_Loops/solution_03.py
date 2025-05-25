# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
number = int(input("Enter the number: "))
for n in range(1,11):
    if n == 5:
        continue
    else:
        print(number*n)

