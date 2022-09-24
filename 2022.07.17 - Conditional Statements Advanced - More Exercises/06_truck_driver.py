season = input()
km = float(input())

km_price = 0

if km <= 5000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.75
    elif season == "Summer":
        km_price = 0.9
    else:
        km_price = 1.05
elif km <= 10000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.95
    elif season == "Summer":
        km_price = 1.1
    else:
        km_price = 1.25
else:
    km_price = 1.45

total = km * km_price * 4 * 0.9

print(f"{total:.2f}")
