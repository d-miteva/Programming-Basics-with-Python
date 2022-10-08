budget = float(input())
season = input()

place = ""
country = ""
price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        country = "Alaska"
        price = budget * 0.65
    else:
        country = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        country = "Alaska"
        price = budget * 0.80
    else:
        country = "Morocco"
        price = budget * 0.60
else:
    place = "Hotel"
    if season == "Summer":
        country = "Alaska"
        price = budget * 0.90
    else:
        country = "Morocco"
        price = budget * 0.90

print(f"{country} - {place} - {price:.2f}")
