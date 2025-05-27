# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_games(**kwargs):
    for key,value in kwargs.items():
        print(f"Keys: {key} Value: {value}") # Formatting string
    
# Usage:
print_games(games1 = "God of war",games2 = "God of war 2",games3 = "God of war 3")

