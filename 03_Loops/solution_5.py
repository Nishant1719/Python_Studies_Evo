# Problem: Given a string, find the first non-repeated character.
# using method count 
input_string = input("Enter the string: ")
result_Str = ""

for char in input_string:
    if input_string.count(char) == 1:
        result_Str = char
        break
    
print(result_Str)
# print(input_string.count('i'))