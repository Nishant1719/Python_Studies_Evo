species = input("Dog or Cat").lower()
animal = species in ["dog","cat"] 
food = None

if animal:
    age = int(input("Age : "))
    if species == "dog":
        food = "Puppy food" if age < 2 else "Senior Puppy food"
    elif species == "cat":
        food = "cat food" if age < 2 else "Senior cat food"
    print(food)
else:
    print("Invalid animal")
    
