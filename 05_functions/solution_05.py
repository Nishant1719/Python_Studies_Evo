# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(username = "Default User"):
    return print("Hello ",username)

user = input("Enter Username : ")
greet(user)
greet()


