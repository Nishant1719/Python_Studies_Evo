# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         return i


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
# yield : # The yield statement is used to produce a value from the generator function.
    # - It stores the state of the function, allowing it to resume where it left off.
    # - This makes generators more memory efficient than regular functions, especially for large datasets.
    # - different from return, which exits the function and does not allow resuming.

# usage example
# print(even_generator(10))  # returned 2 , When used return keyword.
# print(even_generator(10))  # <generator object even_generator at 0x...>
# To get the values from the generator, you can use a loop or convert it to a list.
# print(list(even_generator(10)))  # [2, 4, 6, 8, 10]


for num in even_generator(10):
    print(num)
    
    