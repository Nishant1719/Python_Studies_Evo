weather = input("Enter the weather (Sunny, Rainy, Snowy) : ")

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
else:
    activity = "Stay indoors"

print("Suggested activity:", activity)