# Problem: Keep asking the user for input until they enter a number between 1 and 10.
while True:
    num = int(input("Enter the number: "))
    if  1 <= num <= 10:
        print("Thanks for you input : ",num)
        break
    else:
        print("Please try again")


     

