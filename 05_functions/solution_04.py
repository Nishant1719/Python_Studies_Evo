# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference

v1 , v2= circle_stats(5)
# print("V1 :",math.floor(v1) ," " , "V2 :",math.ceil(v2))
print("V1 :",round(v1,2) ," " , "V2 :",round(v2,2))

# Floor and Ceiling :
    # Floor rounds down to the nearest integer.
    # Ceiling rounds up to the nearest integer.
    # Use Round to round to the nearest integer.
# Example Output:
# V1 : 78  V2 : 31
# Example Output:
# V1 : 78  V2 : 32  
