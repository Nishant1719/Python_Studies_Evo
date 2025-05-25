# Problem: Reverse a string using a loop.
input_string = input("Enter the string: ")
result_string = ""

# for i in range(1,len(input_string)):
#     result_string = result_string + input_string[-i]
    
# print(result_string + input_string[0]) 

# Simple sol:
for char in input_string:
    result_string = char + result_string

print(result_string)