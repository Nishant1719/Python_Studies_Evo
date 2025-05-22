password_len = len(input("Enter password: "))

if password_len > 10 :
    print("Strong")
elif password_len >= 6:
    print("Medium")
else:
    print("Weak")