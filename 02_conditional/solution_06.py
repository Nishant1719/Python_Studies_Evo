distance = float(input("Enter the distance in km: "))

if distance < 3:
    transportation = "Walk"
elif distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"
print("Recommended mode of transportation:", transportation)
