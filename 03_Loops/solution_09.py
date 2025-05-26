# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]

for i in items:
    count = items.count(i)
    if count > 1:
        print(i)
        break
    else:
        print("All unique")
        
