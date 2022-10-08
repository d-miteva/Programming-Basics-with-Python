budget = float(input())
season = input()

class_car = ""
type_car = ""
price = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    else:
        type_car = "Jeep"
        price = budget * 0.65
elif budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    else:
        type_car = "Jeep"
        price = budget * 0.8
else:
    class_car = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.9

print(f"{class_car}")
print(f"{type_car} - {price:.2f}")
