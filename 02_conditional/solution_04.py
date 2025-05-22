# My sol: Experiment
# banana = {
#     "Green" : "Unripe",
#     "Yellow": "Ripe",
#     "Brown": "Overripe"
#     }

# color = input("Enter the colour : ").capitalize()

# for key,value in banana.items():
#     if color == key:
#         print(value)

# Sol : 
fruit = input("Enter fruit : ").capitalize()
color = input("Enter the colour : ").capitalize()


if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Unknown color")