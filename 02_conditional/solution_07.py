coffee_size = input("Enter Coffee Size : ").lower()
extra_shot = bool((input("Extra Shot Yes/No")).lower() == "yes")


if extra_shot:
    order = coffee_size + " with extra shot"
else:
    order = coffee_size + " coffee"
    
print(order)