# Problem: Compute the factorial of a number using a (while loop).
# my sol: from for loop
num = int(input("Enter the number: "))

# result = num 
# for n in range(num):
#     if (num - 1) != 0:
#         result = result * (num - 1)
#         num-=1
# print(result)

# While loop

result = num
while num>1:
     if (num - 1) != 0:
        result = result * (num - 1)
        num -= 1

print(result)