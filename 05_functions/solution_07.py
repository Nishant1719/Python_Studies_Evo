# Problem: Write a function that takes variable number of arguments and returns their sum.
# use it in a list in loops 
    # modern solution

def sum_all(*args): # keyword can be changed as *nishant sill works the same
    print(args) # its a tuple (1, 4, 12, 4, 12, 7, 234)
    # That means you can iterate
    
    for nums in args:
        print(f"Values are {args.index(nums)} : ",nums)
    
    return sum(args)


# print(sum_all(1,4))
# print(sum_all(1,4,5,7,2,3,5))
print(sum_all(1,4,12,4,12,7,234))

# my_numbers = [12,34,123,7,34,12,32]
# print(sum_all(*my_numbers)) # unpacking the values syntax 

