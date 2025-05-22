age = int(input("Enter the age : "))
day = input("Enter day : ")
cost = None

# if age < 18:
#     cost = 8
# else:
#     cost = 12
    
# if day == "wed":
#     cost -= 2
    
# print(f"Bill : {cost}")

# 02--------------------------- Shortcut
cost = 12 if age >= 18 else 8

if day == "wed":
    cost -= 2
    
# print(f"Bill : {cost}")
print("Bill : $",cost)