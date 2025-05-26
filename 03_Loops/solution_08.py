# Problem: Check if a number is prime.
num_input = int(input("Enter the no.: "))
is_prime = True

if num_input > 1:
    for n in range(2,num_input):
        if num_input%n == 0:
            is_prime = False
            break
else:
    print("please enter the no. greater than 1")

if is_prime:
    print("This is a prime no.")
else:
    print("No. is not a prime no.")